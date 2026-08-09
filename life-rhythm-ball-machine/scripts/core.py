"""
life-rhythm-ball-machine 核心引擎
"""
import datetime
import json
import random
import uuid
from pathlib import Path
from typing import Any

from db import (
    load_state, save_state, get_profile, ensure_profile,
    active_profile_id, set_active_profile, get_current_cycle, set_current_cycle,
    SLOT_NAMES, SLOT_LABELS, SLOT_TIMES
)


def _today_str() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d")


def _parse_date(date_str: str) -> datetime.date:
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()


# ──────────────────────────────────────────────
# 1. Profile 管理
# ──────────────────────────────────────────────

def create_profile(state: dict, profile_id: str, name: str = "", emoji: str = "🎱") -> dict:
    profile = ensure_profile(state, profile_id, name or profile_id, emoji)
    if state.get("active_profile") is None:
        state["active_profile"] = profile_id
    return profile


def list_profiles(state: dict) -> list[dict]:
    return [
        {"id": pid, "name": p["name"], "emoji": p["emoji"],
         "has_cycle": p["current_cycle"] is not None}
        for pid, p in state["profiles"].items()
    ]


def switch_profile(state: dict, profile_id: str) -> bool:
    if profile_id not in state["profiles"]:
        return False
    state["active_profile"] = profile_id
    return True


# ──────────────────────────────────────────────
# 2. 球库管理
# ──────────────────────────────────────────────

def add_ball_to_library(state: dict, category: str, content: str,
                        energy_level: str = "medium", tags: list[str] | None = None,
                        source: str = "user", profile_id: str | None = None) -> dict:
    profile = get_profile(state, profile_id)
    if not profile:
        raise ValueError("Profile not found")
    if category not in profile["ball_library"]:
        profile["ball_library"][category] = []
    ball = {
        "id": str(uuid.uuid4())[:8],
        "content": content,
        "energy_level": energy_level,
        "tags": tags or [],
        "source": source,
        "added_at": _today_str()
    }
    profile["ball_library"][category].append(ball)
    return ball


def list_library(state: dict, category: str | None = None,
                 profile_id: str | None = None) -> dict | list:
    profile = get_profile(state, profile_id)
    if not profile:
        raise ValueError("Profile not found")
    lib = profile["ball_library"]
    if category:
        return lib.get(category, [])
    return lib


def remove_ball_from_library(state: dict, category: str, ball_id: str,
                              profile_id: str | None = None) -> bool:
    profile = get_profile(state, profile_id)
    if not profile or category not in profile["ball_library"]:
        return False
    balls = profile["ball_library"][category]
    for i, b in enumerate(balls):
        if b["id"] == ball_id:
            balls.pop(i)
            return True
    return False


# ──────────────────────────────────────────────
# 3. 收藏夹导入
# ──────────────────────────────────────────────

def import_collection(state: dict, category: str, source_path: str,
                      source_tag: str | None = None,
                      energy_level: str = "medium",
                      profile_id: str | None = None) -> dict:
    """
    支持格式：
    - 纯文本列表（每行一个）
    - JSON 数组 ["item1", "item2", ...]
    - Markdown 清单（- item / * item / 1. item）
    """
    path = Path(source_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {source_path}")
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()

    items: list[str] = []
    text = raw.strip()
    if text.startswith("["):
        # JSON array
        try:
            items = [str(x) for x in json.loads(text) if x]
        except json.JSONDecodeError:
            pass
    if not items:
        # Markdown / plain text
        for line in text.splitlines():
            line = line.strip()
            if not line:
                continue
            # 去掉 markdown list markers
            for prefix in ("- ", "* ", "+ ", "• "):
                if line.startswith(prefix):
                    line = line[len(prefix):]
                    break
            else:
                # 数字列表 "1. "
                import re
                line = re.sub(r"^\d+\.\\s*", "", line)
            line = line.strip()
            if line:
                items.append(line)

    tag = source_tag or f"#{path.stem}"
    added = []
    for item in items:
        ball = add_ball_to_library(state, category, item,
                                   energy_level=energy_level,
                                   tags=[tag],
                                   source=tag,
                                   profile_id=profile_id)
        added.append(ball)
    return {"imported_count": len(added), "items": added}


# ──────────────────────────────────────────────
# 4. 趣味球库
# ──────────────────────────────────────────────

def _load_fun_balls() -> dict[str, list[dict]]:
    fun_path = Path(__file__).parent / "fun_balls.json"
    if not fun_path.exists():
        return {}
    with open(fun_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _make_fun_ball(category: str, data: dict) -> dict:
    return {
        "id": f"fun_{str(uuid.uuid4())[:6]}",
        "content": data["content"],
        "energy_level": data.get("energy_level", "medium"),
        "tags": ["#趣味球"],
        "source": "fun",
        "added_at": _today_str(),
        "category": category
    }


# ──────────────────────────────────────────────
# 5. 球池生成（比例装填）
# ──────────────────────────────────────────────

def allocate_balls(total: int, proportions: dict[str, int]) -> dict[str, int]:
    """
    按比例分配整数球数，误差不超过 1。
    proportions: {category: percentage}
    使用最大余数法保证 0% 的类别一定分到 0。
    """
    if not proportions:
        raise ValueError("Proportions cannot be empty")
    total_pct = sum(proportions.values())
    if total_pct != 100:
        raise ValueError(f"Proportions must sum to 100, got {total_pct}")

    # 理论值
    raw = {cat: total * pct / 100 for cat, pct in proportions.items()}
    allocated = {cat: int(v) for cat, v in raw.items()}
    remaining = total - sum(allocated.values())

    # 按小数部分从大到小分配余数（仅对 >0% 的类别）
    if remaining > 0:
        remainders = sorted(
            [(cat, raw[cat] - allocated[cat]) for cat in proportions if proportions[cat] > 0],
            key=lambda x: x[1], reverse=True
        )
        for i in range(remaining):
            cat = remainders[i % len(remainders)][0]
            allocated[cat] += 1

    return allocated


def fill_cycle(state: dict, days: int, proportions: dict[str, int],
               min_energy: str | None = None, fun_ball_count: int = 0,
               profile_id: str | None = None) -> dict:
    """
    装填一个新周期。
    - days: 周期天数
    - proportions: {category: percentage}，总和必须 100
    - min_energy: 'low'|'medium'|'high'，每天保底一个该能量等级的球
    - fun_ball_count: 混入的趣味球数量
    """
    profile = get_profile(state, profile_id)
    if not profile:
        raise ValueError("Profile not found")

    # 如果有正在进行的周期，先归档
    old_cycle = profile.get("current_cycle")
    if old_cycle and not _is_cycle_finished(old_cycle):
        archive_cycle(state, profile_id=profile_id)

    total_balls = days * 3
    allocation = allocate_balls(total_balls, proportions)

    # 收集球源
    library = profile["ball_library"]
    fun_balls_db = _load_fun_balls()

    pool: list[dict] = []
    for cat, count in allocation.items():
        if count <= 0:
            continue
        # 仅从用户球库取球（趣味球不用于补充枯竭）
        sources: list[dict] = list(library.get(cat, []))

        if len(sources) < count:
            raise ValueError(
                f"球库枯竭：类别「{cat}」需要 {count} 个球，但用户球库只有 {len(sources)} 个。"
                f"请先补充球库或减少该类比例。"
            )

        # 不重复抽取
        chosen = random.sample(sources, count)
        for ball in chosen:
            b = dict(ball)
            b["category"] = cat
            if "id" not in b:
                b["id"] = str(uuid.uuid4())[:8]
            pool.append(b)

    # 混入额外趣味球（替换掉已有球）
    if fun_ball_count > 0 and pool:
        all_fun = []
        for cat, items in fun_balls_db.items():
            all_fun.extend([_make_fun_ball(cat, d) for d in items])
        if all_fun:
            replace_count = min(fun_ball_count, len(pool))
            indices = random.sample(range(len(pool)), replace_count)
            fun_samples = random.sample(all_fun, replace_count)
            for idx, fun_ball in zip(indices, fun_samples):
                pool[idx] = fun_ball

    random.shuffle(pool)

    # 保底低能量球
    if min_energy:
        _ensure_min_energy(pool, days, min_energy)

    start_date = _today_str()
    end_date = (_parse_date(start_date) + datetime.timedelta(days=days - 1)).isoformat()

    cycle = {
        "start_date": start_date,
        "end_date": end_date,
        "total_days": days,
        "total_balls": total_balls,
        "proportion": proportions,
        "ball_pool": pool,
        "schedule": {},
        "config": {
            "min_energy": min_energy,
            "fun_ball_count": fun_ball_count
        }
    }

    profile["current_cycle"] = cycle
    profile["stats"]["total_cycles"] = profile["stats"]["total_cycles"] + 1
    return cycle


def _ensure_min_energy(pool: list[dict], days: int, min_level: str) -> None:
    """确保每天三球中至少有一个 <= min_level 能量等级的球"""
    energy_order = {"low": 0, "medium": 1, "high": 2}
    threshold = energy_order.get(min_level, 1)

    for day_idx in range(days):
        start = day_idx * 3
        end = start + 3
        if end > len(pool):
            break
        day_balls = pool[start:end]
        has_low = any(
            energy_order.get(b.get("energy_level", "medium"), 1) <= threshold
            for b in day_balls
        )
        if not has_low:
            # 找一个低能量球替换
            low_candidates = [
                i for i, b in enumerate(pool)
                if i < start or i >= end and
                energy_order.get(b.get("energy_level", "medium"), 1) <= threshold
            ]
            if low_candidates:
                swap_in = random.choice(low_candidates)
                # 与当天第一个球交换
                pool[start], pool[swap_in] = pool[swap_in], pool[start]


# ──────────────────────────────────────────────
# 6. 每日三球抽取
# ──────────────────────────────────────────────

def draw_today(state: dict, profile_id: str | None = None,
               force: bool = False) -> dict:
    """
    生成或返回今日三球。
    - force: 如果今日已生成，是否重新生成（正常不允许，仅测试用）
    """
    profile = get_profile(state, profile_id)
    if not profile:
        raise ValueError("Profile not found")
    cycle = profile.get("current_cycle")
    if not cycle:
        raise ValueError("No active cycle. Use `fill` first.")

    today = _today_str()
    schedule = cycle.setdefault("schedule", {})

    if today in schedule and not force:
        return schedule[today]

    # 计算今天是周期的第几天
    day_index = (_parse_date(today) - _parse_date(cycle["start_date"])).days
    if day_index < 0:
        raise ValueError("Current date is before cycle start date")
    if day_index >= cycle["total_days"]:
        raise ValueError("Cycle has ended. Please fill a new cycle.")

    start_idx = day_index * 3
    end_idx = start_idx + 3
    if end_idx > len(cycle["ball_pool"]):
        raise ValueError("Ball pool exhausted")

    day_balls = cycle["ball_pool"][start_idx:end_idx]
    schedule[today] = {
        "morning": {"ball": day_balls[0], "status": "pending", "completed_at": None},
        "afternoon": {"ball": day_balls[1], "status": "pending", "completed_at": None},
        "evening": {"ball": day_balls[2], "status": "pending", "completed_at": None},
        "generated_at": datetime.datetime.now().isoformat()
    }
    return schedule[today]


def get_today(state: dict, profile_id: str | None = None) -> dict | None:
    """获取今日三球，未生成则返回 None"""
    profile = get_profile(state, profile_id)
    if not profile:
        return None
    cycle = profile.get("current_cycle")
    if not cycle:
        return None
    today = _today_str()
    return cycle.get("schedule", {}).get(today)


# ──────────────────────────────────────────────
# 7. 完成 / 跳过（不可变性）
# ──────────────────────────────────────────────

def complete_slot(state: dict, slot: str, profile_id: str | None = None) -> dict:
    """完成某个场次"""
    if slot not in SLOT_NAMES:
        raise ValueError(f"Invalid slot: {slot}. Must be one of {SLOT_NAMES}")
    profile = get_profile(state, profile_id)
    if not profile:
        raise ValueError("Profile not found")
    cycle = profile.get("current_cycle")
    if not cycle:
        raise ValueError("No active cycle")

    today = _today_str()
    schedule = cycle.get("schedule", {})
    if today not in schedule:
        raise ValueError("Today's schedule has not been drawn yet. Use `draw` first.")

    entry = schedule[today][slot]
    if entry["status"] != "pending":
        raise ValueError(f"Cannot complete: slot is already {entry['status']}")

    entry["status"] = "completed"
    entry["completed_at"] = datetime.datetime.now().isoformat()

    # 更新统计
    stats = profile["stats"]
    stats["total_balls_completed"] += 1

    # 检查今日是否全部完成，更新 streak
    if _is_today_all_done(schedule[today]):
        stats["current_streak"] += 1
        if stats["current_streak"] > stats["max_streak"]:
            stats["max_streak"] = stats["current_streak"]

    return entry


def skip_slot(state: dict, slot: str, profile_id: str | None = None) -> dict:
    """跳过某个场次"""
    if slot not in SLOT_NAMES:
        raise ValueError(f"Invalid slot: {slot}. Must be one of {SLOT_NAMES}")
    profile = get_profile(state, profile_id)
    if not profile:
        raise ValueError("Profile not found")
    cycle = profile.get("current_cycle")
    if not cycle:
        raise ValueError("No active cycle")

    today = _today_str()
    schedule = cycle.get("schedule", {})
    if today not in schedule:
        raise ValueError("Today's schedule has not been drawn yet. Use `draw` first.")

    entry = schedule[today][slot]
    if entry["status"] != "pending":
        raise ValueError(f"Cannot skip: slot is already {entry['status']}")

    entry["status"] = "skipped"
    entry["completed_at"] = datetime.datetime.now().isoformat()

    # 更新统计
    stats = profile["stats"]
    stats["total_balls_skipped"] += 1
    # 跳过断掉 streak
    if not _is_today_all_done(schedule[today]):
        stats["current_streak"] = 0

    return entry


def _is_today_all_done(day_schedule: dict) -> bool:
    return all(
        day_schedule[s]["status"] == "completed"
        for s in SLOT_NAMES
    )


# ──────────────────────────────────────────────
# 8. 周期管理
# ──────────────────────────────────────────────

def archive_cycle(state: dict, profile_id: str | None = None) -> dict:
    """归档当前周期到历史"""
    profile = get_profile(state, profile_id)
    if not profile:
        raise ValueError("Profile not found")
    cycle = profile.get("current_cycle")
    if not cycle:
        raise ValueError("No active cycle to archive")

    # 计算周期完成统计
    summary = _summarize_cycle(cycle)
    archived = {
        "archived_at": _today_str(),
        "cycle": cycle,
        "summary": summary
    }
    profile["history"].append(archived)
    profile["current_cycle"] = None
    profile["stats"]["current_streak"] = 0
    return archived


def _is_cycle_finished(cycle: dict) -> bool:
    today = _today_str()
    return today > cycle.get("end_date", "")


def _summarize_cycle(cycle: dict) -> dict:
    schedule = cycle.get("schedule", {})
    completed = 0
    skipped = 0
    pending = 0
    category_counts: dict[str, int] = {}

    for day, slots in schedule.items():
        for slot in SLOT_NAMES:
            entry = slots.get(slot, {})
            status = entry.get("status", "pending")
            if status == "completed":
                completed += 1
            elif status == "skipped":
                skipped += 1
            else:
                pending += 1
            cat = entry.get("ball", {}).get("category", "unknown")
            category_counts[cat] = category_counts.get(cat, 0) + 1

    total = completed + skipped + pending
    return {
        "total_balls": total,
        "completed": completed,
        "skipped": skipped,
        "pending": pending,
        "completion_rate": round(completed / total * 100, 1) if total else 0,
        "category_distribution": category_counts
    }


def get_cycle_status(state: dict, profile_id: str | None = None) -> dict | None:
    profile = get_profile(state, profile_id)
    if not profile:
        return None
    cycle = profile.get("current_cycle")
    if not cycle:
        return None

    today = _today_str()
    day_index = (_parse_date(today) - _parse_date(cycle["start_date"])).days
    total_days = cycle["total_days"]
    remaining = total_days - day_index - 1

    summary = _summarize_cycle(cycle)
    return {
        "start_date": cycle["start_date"],
        "end_date": cycle["end_date"],
        "today": today,
        "day_number": day_index + 1,
        "total_days": total_days,
        "remaining_days": max(0, remaining),
        "progress_pct": round((day_index + 1) / total_days * 100, 1),
        "summary": summary,
        "is_today_drawn": today in cycle.get("schedule", {})
    }


# ──────────────────────────────────────────────
# 9. 统计与报告
# ──────────────────────────────────────────────

def get_stats(state: dict, profile_id: str | None = None) -> dict:
    profile = get_profile(state, profile_id)
    if not profile:
        raise ValueError("Profile not found")
    return dict(profile["stats"])


def generate_report(state: dict, profile_id: str | None = None) -> dict:
    """生成当前周期 + 历史的综合报告"""
    profile = get_profile(state, profile_id)
    if not profile:
        raise ValueError("Profile not found")

    report = {
        "profile_name": profile["name"],
        "generated_at": datetime.datetime.now().isoformat(),
        "current_cycle": None,
        "history_summary": [],
        "overall_stats": dict(profile["stats"])
    }

    cycle = profile.get("current_cycle")
    if cycle:
        report["current_cycle"] = {
            "period": f"{cycle['start_date']} ~ {cycle['end_date']}",
            "summary": _summarize_cycle(cycle)
        }

    for h in profile.get("history", []):
        report["history_summary"].append({
            "archived_at": h["archived_at"],
            "period": f"{h['cycle']['start_date']} ~ {h['cycle']['end_date']}",
            "summary": h["summary"]
        })

    return report


# ──────────────────────────────────────────────
# 10. 早报
# ──────────────────────────────────────────────

def generate_morning_brief(state: dict, profile_id: str | None = None) -> str:
    """生成早报文本"""
    profile = get_profile(state, profile_id)
    if not profile:
        return "[错误] 未找到角色"

    lines = [f"🌅 {profile['name']} 的今日球机早报"]
    lines.append(f"日期: {_today_str()}")
    lines.append("")

    # 今日三球
    today_schedule = get_today(state, profile_id)
    if today_schedule:
        lines.append("📋 今日三球:")
        for slot in SLOT_NAMES:
            entry = today_schedule[slot]
            ball = entry["ball"]
            status_icon = {"pending": "⏳", "completed": "✅", "skipped": "⏭️"}
            icon = status_icon.get(entry["status"], "❓")
            lines.append(
                f"  {icon} {SLOT_LABELS[slot]} ({SLOT_TIMES[slot]})"
                f" [{ball.get('category', '?')}] {ball['content']}"
            )
    else:
        lines.append("📋 今日三球尚未抽取，使用 `draw` 踩一脚！")

    # 周期进度
    cycle = profile.get("current_cycle")
    if cycle:
        status = get_cycle_status(state, profile_id)
        if status:
            bar_len = 20
            filled = int(status["progress_pct"] / 100 * bar_len)
            bar = "█" * filled + "░" * (bar_len - filled)
            lines.append("")
            lines.append(f"📊 周期进度: [{bar}] {status['progress_pct']}%")
            lines.append(f"   第 {status['day_number']}/{status['total_days']} 天")

    # 昨日状态
    yesterday = (_parse_date(_today_str()) - datetime.timedelta(days=1)).isoformat()
    if cycle and yesterday in cycle.get("schedule", {}):
        yday = cycle["schedule"][yesterday]
        y_completed = sum(1 for s in SLOT_NAMES if yday[s]["status"] == "completed")
        y_skipped = sum(1 for s in SLOT_NAMES if yday[s]["status"] == "skipped")
        lines.append("")
        lines.append(f"📈 昨日: ✅{y_completed}  ⏭️{y_skipped}  ⏳{3 - y_completed - y_skipped}")

    # 连续记录
    streak = profile["stats"]["current_streak"]
    max_streak = profile["stats"]["max_streak"]
    lines.append("")
    lines.append(f"🔥 连续完成天数: {streak} (最高: {max_streak})")
    lines.append("")
    lines.append("💡 信任契约: 不要想，直接做。改日程的权限在上一个你手里，不在现在的你手里。")

    return "\n".join(lines)

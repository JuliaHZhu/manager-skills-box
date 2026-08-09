"""
life-rhythm-ball-machine 数据库层
单文件 JSON 持久化，多 profile 隔离
"""
import json
import os
from pathlib import Path
from typing import Any

DEFAULT_STATE = {
    "profiles": {},
    "active_profile": None
}

DEFAULT_PROFILE = {
    "name": "",
    "emoji": "🎱",
    "created_at": "",
    "ball_library": {},
    "current_cycle": None,
    "history": [],
    "stats": {
        "total_cycles": 0,
        "total_balls_completed": 0,
        "total_balls_skipped": 0,
        "current_streak": 0,
        "max_streak": 0
    }
}

DEFAULT_CYCLE = {
    "start_date": "",
    "end_date": "",
    "total_days": 0,
    "total_balls": 0,
    "proportion": {},
    "ball_pool": [],
    "schedule": {},
    "config": {
        "min_energy": None,
        "fun_ball_count": 0
    }
}

SLOT_NAMES = ["morning", "afternoon", "evening"]
SLOT_LABELS = {"morning": "早场", "afternoon": "午场", "evening": "晚场"}
SLOT_TIMES = {
    "morning": "08:00-11:00",
    "afternoon": "13:00-17:00",
    "evening": "19:00-23:00"
}


def get_db_path() -> Path:
    """返回数据库文件路径"""
    # 优先使用环境变量，否则使用 workspace 下的 data 目录
    env_path = os.environ.get("LIFE_RHYTHM_DB")
    if env_path:
        return Path(env_path)
    base = Path(__file__).parent.parent.parent.parent  # workspace root
    data_dir = base / "data"
    data_dir.mkdir(exist_ok=True)
    return data_dir / "life-rhythm-state.json"


def load_state(db_path: Path | None = None) -> dict:
    """加载完整状态"""
    path = db_path or get_db_path()
    if not path.exists():
        return {"profiles": {}, "active_profile": None}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {"profiles": {}, "active_profile": None}


def save_state(state: dict, db_path: Path | None = None) -> None:
    """保存完整状态"""
    path = db_path or get_db_path()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def get_profile(state: dict, profile_id: str | None = None) -> dict | None:
    """获取指定 profile，不传则获取 active"""
    pid = profile_id or state.get("active_profile")
    if not pid:
        return None
    return state["profiles"].get(pid)


def ensure_profile(state: dict, profile_id: str, name: str = "", emoji: str = "🎱") -> dict:
    """确保 profile 存在，不存在则创建（深拷贝避免模块级默认值污染）"""
    if profile_id not in state["profiles"]:
        import datetime
        profile = {
            "name": name or profile_id,
            "emoji": emoji,
            "created_at": datetime.datetime.now().isoformat(),
            "ball_library": {},
            "current_cycle": None,
            "history": [],
            "stats": {
                "total_cycles": 0,
                "total_balls_completed": 0,
                "total_balls_skipped": 0,
                "current_streak": 0,
                "max_streak": 0
            }
        }
        state["profiles"][profile_id] = profile
    return state["profiles"][profile_id]


def active_profile_id(state: dict) -> str | None:
    return state.get("active_profile")


def set_active_profile(state: dict, profile_id: str) -> None:
    state["active_profile"] = profile_id


def get_current_cycle(state: dict, profile_id: str | None = None) -> dict | None:
    """获取当前周期"""
    profile = get_profile(state, profile_id)
    if not profile:
        return None
    return profile.get("current_cycle")


def set_current_cycle(state: dict, cycle: dict, profile_id: str | None = None) -> None:
    """设置当前周期"""
    profile = get_profile(state, profile_id)
    if not profile:
        return
    profile["current_cycle"] = cycle

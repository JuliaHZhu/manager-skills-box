#!/usr/bin/env python3
"""
life-rhythm-ball-machine CLI
"""
import argparse
import json
import sys
from pathlib import Path

from db import load_state, save_state
from core import (
    create_profile, list_profiles, switch_profile,
    add_ball_to_library, list_library, remove_ball_from_library, import_collection,
    fill_cycle, draw_today, get_today, complete_slot, skip_slot,
    get_cycle_status, get_stats, generate_report, generate_morning_brief,
    SLOT_NAMES, SLOT_LABELS, SLOT_TIMES
)


def _active_pid(state):
    return state.get("active_profile")


def cmd_profile_create(args):
    state = load_state()
    pid = args.id
    create_profile(state, pid, name=args.name or pid, emoji=args.emoji)
    save_state(state)
    print(f"✅ 角色已创建: {pid} ({state['profiles'][pid]['emoji']} {state['profiles'][pid]['name']})")
    if state.get("active_profile") == pid:
        print(f"   已自动设为当前角色")


def cmd_profile_list(args):
    state = load_state()
    profiles = list_profiles(state)
    active = _active_pid(state)
    if not profiles:
        print("暂无角色。使用 `profile create <id>` 创建")
        return
    for p in profiles:
        marker = "👉 " if p["id"] == active else "   "
        cycle_marker = "🔄 有进行中的周期" if p["has_cycle"] else ""
        print(f"{marker}{p['emoji']} {p['name']} (id: {p['id']}) {cycle_marker}")


def cmd_profile_switch(args):
    state = load_state()
    if switch_profile(state, args.id):
        save_state(state)
        p = state["profiles"][args.id]
        print(f"✅ 已切换到: {p['emoji']} {p['name']} ({args.id})")
    else:
        print(f"❌ 角色不存在: {args.id}")
        sys.exit(1)


def cmd_library_add(args):
    state = load_state()
    ball = add_ball_to_library(
        state, args.category, args.content,
        energy_level=args.energy,
        tags=args.tags.split(",") if args.tags else [],
        profile_id=args.profile
    )
    save_state(state)
    print(f"✅ 已添加球到「{args.category}」: {ball['content'][:40]}...")


def cmd_library_list(args):
    state = load_state()
    result = list_library(state, category=args.category, profile_id=args.profile)
    if isinstance(result, dict):
        if not result:
            print("球库为空")
            return
        total = sum(len(v) for v in result.values())
        print(f"📚 球库总计: {total} 个球")
        for cat, balls in result.items():
            print(f"\n  📂 {cat} ({len(balls)} 个)")
            for b in balls[:10]:
                tags = " ".join(b.get("tags", []))
                print(f"     [{b['energy_level']}] {b['content'][:50]}... {tags}")
            if len(balls) > 10:
                print(f"     ... 还有 {len(balls) - 10} 个")
    else:
        if not result:
            print(f"「{args.category}」类别为空")
            return
        print(f"📂 {args.category} ({len(result)} 个)")
        for b in result[:20]:
            tags = " ".join(b.get("tags", []))
            print(f"   [{b['energy_level']}] {b['content'][:60]}... {tags}")


def cmd_library_remove(args):
    state = load_state()
    ok = remove_ball_from_library(state, args.category, args.ball_id, profile_id=args.profile)
    save_state(state)
    if ok:
        print(f"✅ 已删除球")
    else:
        print(f"❌ 未找到该球")


def cmd_library_import(args):
    state = load_state()
    result = import_collection(
        state, args.category, args.file,
        source_tag=args.tag,
        energy_level=args.energy,
        profile_id=args.profile
    )
    save_state(state)
    print(f"✅ 成功导入 {result['imported_count']} 个球到「{args.category}」")


def cmd_fill(args):
    state = load_state()
    # 解析比例: 读书:30,休息:30,探索:20,社交:20
    proportions = {}
    for part in args.proportion.split(","):
        cat, pct = part.split(":")
        proportions[cat.strip()] = int(pct.strip())

    print("🎱 生活节律球机 —— 装填")
    print(f"   周期: {args.days} 天")
    print(f"   比例: {args.proportion}")
    if args.min_energy:
        print(f"   能量保底: 每天至少 1 个 {args.min_energy} 能量球")
    if args.fun_balls:
        print(f"   趣味球: 混入 {args.fun_balls} 个")
    print("")
    print("⚠️  信任契约: 装填完成后，在周期结束之前，你将无法修改任何日程。")
    print("    相信此刻的判断。")
    print("")

    try:
        cycle = fill_cycle(
            state, days=args.days, proportions=proportions,
            min_energy=args.min_energy,
            fun_ball_count=args.fun_balls,
            profile_id=args.profile
        )
        save_state(state)
        print(f"✅ 装填完成！周期: {cycle['start_date']} ~ {cycle['end_date']}")
        print(f"   总计 {cycle['total_balls']} 个球，按 {args.proportion} 分配")
    except ValueError as e:
        print(f"❌ 装填失败: {e}")
        sys.exit(1)


def cmd_draw(args):
    state = load_state()
    try:
        today = draw_today(state, profile_id=args.profile)
        save_state(state)
        print("🎱 踩一脚！球机运转中...")
        print("=" * 50)
        for slot in SLOT_NAMES:
            entry = today[slot]
            ball = entry["ball"]
            print(f"\n  🕐 {SLOT_LABELS[slot]} ({SLOT_TIMES[slot]})")
            print(f"     [{ball.get('category', '?')}] {ball['content']}")
            print(f"     能量: {ball.get('energy_level', 'medium')} | 来源: {ball.get('source', 'user')}")
            if ball.get("tags"):
                print(f"     标签: {' '.join(ball['tags'])}")
        print("\n" + "=" * 50)
        print("💡 不要想，直接做。改日程的权限在上一个你手里，不在现在的你手里。")
    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)


def cmd_today(args):
    state = load_state()
    today = get_today(state, profile_id=args.profile)
    if not today:
        print("📭 今日三球尚未抽取。使用 `draw` 踩一脚！")
        return
    print("📋 今日三球:")
    for slot in SLOT_NAMES:
        entry = today[slot]
        ball = entry["ball"]
        status_icon = {"pending": "⏳", "completed": "✅", "skipped": "⏭️"}
        icon = status_icon.get(entry["status"], "❓")
        print(f"  {icon} {SLOT_LABELS[slot]} [{ball.get('category', '?')}] {ball['content'][:40]}...")


def cmd_complete(args):
    state = load_state()
    try:
        entry = complete_slot(state, args.slot, profile_id=args.profile)
        save_state(state)
        ball = entry["ball"]
        print(f"✅ 完成 {SLOT_LABELS[args.slot]}: [{ball.get('category', '?')}] {ball['content'][:40]}...")
    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)


def cmd_skip(args):
    state = load_state()
    try:
        entry = skip_slot(state, args.slot, profile_id=args.profile)
        save_state(state)
        ball = entry["ball"]
        print(f"⏭️  跳过 {SLOT_LABELS[args.slot]}: [{ball.get('category', '?')}] {ball['content'][:40]}...")
    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)


def cmd_status(args):
    state = load_state()
    status = get_cycle_status(state, profile_id=args.profile)
    if not status:
        print("📭 没有进行中的周期。使用 `fill` 装填新周期")
        return
    print(f"🔄 周期状态: {status['start_date']} ~ {status['end_date']}")
    bar_len = 30
    filled = int(status["progress_pct"] / 100 * bar_len)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"   进度: [{bar}] {status['progress_pct']}%")
    print(f"   第 {status['day_number']}/{status['total_days']} 天，还剩 {status['remaining_days']} 天")
    s = status["summary"]
    print(f"   完成: {s['completed']} | 跳过: {s['skipped']} | 待定: {s['pending']}")
    print(f"   完成率: {s['completion_rate']}%")


def cmd_stats(args):
    state = load_state()
    stats = get_stats(state, profile_id=args.profile)
    print("📊 生涯统计")
    print(f"   总周期数: {stats['total_cycles']}")
    print(f"   总完成球: {stats['total_balls_completed']}")
    print(f"   总跳过球: {stats['total_balls_skipped']}")
    print(f"   当前连续: {stats['current_streak']} 天")
    print(f"   最高连续: {stats['max_streak']} 天")


def cmd_report(args):
    state = load_state()
    report = generate_report(state, profile_id=args.profile)
    print(f"📑 {report['profile_name']} 的综合报告")
    print(f"   生成时间: {report['generated_at']}")
    print(f"   总周期数: {report['overall_stats']['total_cycles']}")
    print(f"   总完成球: {report['overall_stats']['total_balls_completed']}")
    print(f"   总跳过球: {report['overall_stats']['total_balls_skipped']}")
    print(f"   最高连续: {report['overall_stats']['max_streak']} 天")
    if report["current_cycle"]:
        print(f"\n🔄 当前周期: {report['current_cycle']['period']}")
        s = report["current_cycle"]["summary"]
        print(f"   完成率: {s['completion_rate']}% ({s['completed']}/{s['total_balls']})")
    if report["history_summary"]:
        print(f"\n📚 历史周期 ({len(report['history_summary'])} 个):")
        for h in report["history_summary"][-5:]:
            print(f"   {h['period']} — 完成率 {h['summary']['completion_rate']}%")


def cmd_cron(args):
    state = load_state()
    text = generate_morning_brief(state, profile_id=args.profile)
    print(text)


def main():
    parser = argparse.ArgumentParser(
        description="🎱 生活节律球机 —— 比例化作息、每日三球、不可修改的执行系统"
    )
    parser.add_argument("--profile", "-p", help="指定角色 ID（默认使用当前角色）")
    sub = parser.add_subparsers(dest="command", help="命令")

    # profile
    p_profile = sub.add_parser("profile", help="角色管理")
    p_profile_sub = p_profile.add_subparsers(dest="subcmd")
    p_create = p_profile_sub.add_parser("create", help="创建角色")
    p_create.add_argument("id", help="角色 ID")
    p_create.add_argument("--name", "-n", help="显示名称")
    p_create.add_argument("--emoji", "-e", default="🎱", help="头像 emoji")
    p_profile_sub.add_parser("list", help="列出角色")
    p_switch = p_profile_sub.add_parser("switch", help="切换角色")
    p_switch.add_argument("id", help="角色 ID")

    # library
    p_lib = sub.add_parser("library", help="球库管理")
    p_lib_sub = p_lib.add_subparsers(dest="subcmd")
    p_add = p_lib_sub.add_parser("add", help="添加球")
    p_add.add_argument("category", help="类别")
    p_add.add_argument("content", help="内容")
    p_add.add_argument("--energy", "-e", default="medium", choices=["low", "medium", "high"])
    p_add.add_argument("--tags", "-t", help="标签，逗号分隔")
    p_list = p_lib_sub.add_parser("list", help="查看球库")
    p_list.add_argument("--category", "-c", help="指定类别")
    p_remove = p_lib_sub.add_parser("remove", help="删除球")
    p_remove.add_argument("category", help="类别")
    p_remove.add_argument("ball_id", help="球 ID")
    p_import = p_lib_sub.add_parser("import", help="导入收藏夹")
    p_import.add_argument("category", help="目标类别")
    p_import.add_argument("file", help="文件路径")
    p_import.add_argument("--tag", help="来源标签（默认使用文件名）")
    p_import.add_argument("--energy", "-e", default="medium", choices=["low", "medium", "high"])

    # fill
    p_fill = sub.add_parser("fill", help="装填新周期")
    p_fill.add_argument("--days", "-d", type=int, required=True, help="周期天数")
    p_fill.add_argument("--proportion", "-r", required=True,
                        help="比例，格式: 读书:30,休息:30,探索:20,社交:20")
    p_fill.add_argument("--min-energy", choices=["low", "medium", "high"],
                        help="每天保底能量等级")
    p_fill.add_argument("--fun-balls", type=int, default=0, help="混入趣味球数量")

    # draw / today
    sub.add_parser("draw", help="踩一脚 —— 抽取/查看今日三球")
    sub.add_parser("today", help="查看今日三球状态")

    # complete / skip
    p_comp = sub.add_parser("complete", help="完成场次")
    p_comp.add_argument("slot", choices=SLOT_NAMES, help="场次")
    p_skip = sub.add_parser("skip", help="跳过场次")
    p_skip.add_argument("slot", choices=SLOT_NAMES, help="场次")

    # status / stats / report / cron
    sub.add_parser("status", help="查看周期状态")
    sub.add_parser("stats", help="查看生涯统计")
    sub.add_parser("report", help="生成综合报告")
    sub.add_parser("cron", help="生成早报")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    if args.command == "profile":
        if args.subcmd == "create":
            cmd_profile_create(args)
        elif args.subcmd == "list":
            cmd_profile_list(args)
        elif args.subcmd == "switch":
            cmd_profile_switch(args)
        else:
            p_profile.print_help()
    elif args.command == "library":
        if args.subcmd == "add":
            cmd_library_add(args)
        elif args.subcmd == "list":
            cmd_library_list(args)
        elif args.subcmd == "remove":
            cmd_library_remove(args)
        elif args.subcmd == "import":
            cmd_library_import(args)
        else:
            p_lib.print_help()
    elif args.command == "fill":
        cmd_fill(args)
    elif args.command == "draw":
        cmd_draw(args)
    elif args.command == "today":
        cmd_today(args)
    elif args.command == "complete":
        cmd_complete(args)
    elif args.command == "skip":
        cmd_skip(args)
    elif args.command == "status":
        cmd_status(args)
    elif args.command == "stats":
        cmd_stats(args)
    elif args.command == "report":
        cmd_report(args)
    elif args.command == "cron":
        cmd_cron(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

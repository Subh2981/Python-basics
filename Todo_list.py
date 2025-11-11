
"""
todo.py - simple CLI to-do list (single-file, no external deps)

Usage examples:
  python todo_list.py add "Buy milk" --due 2025-10-25 --priority 2
  python todo_list.py list
  python todo_list.py done 3
  python todo_list.py edit 2 --title "Call Alice" --due 2025-10-30
  python todo_list.py delete 5
  python todo_list.py search "milk"
"""

from __future__ import annotations
import argparse
import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional

DATA_PATH = Path.home() / ".todo.json"
DATE_FMT = "%Y-%m-%d"  # ISO-ish date format

@dataclass
class Task:
    id: int
    title: str
    created: str  # ISO date/time string
    due: Optional[str] = None  # ISO date string YYYY-MM-DD
    priority: int = 3  # 1-high .. 5-low
    done: bool = False
    notes: Optional[str] = None

def load_tasks() -> List[Task]:
    if not DATA_PATH.exists():
        return []
    try:
        raw = json.loads(DATA_PATH.read_text(encoding="utf-8"))
        return [Task(**r) for r in raw]
    except Exception:
        return []

def save_tasks(tasks: List[Task]) -> None:
    DATA_PATH.write_text(json.dumps([asdict(t) for t in tasks], indent=2), encoding="utf-8")

def next_id(tasks: List[Task]) -> int:
    return max((t.id for t in tasks), default=0) + 1

def parse_date(s: Optional[str]) -> Optional[str]:
    if not s:
        return None
    s = s.strip()
    try:
        # accept YYYY-MM-DD only for simplicity
        datetime.strptime(s, DATE_FMT)
        return s
    except ValueError:
        raise argparse.ArgumentTypeError(f"Date must be YYYY-MM-DD, got: {s}")

def display_tasks(tasks: List[Task], show_all=False) -> None:
    if not tasks:
        print("No tasks found.")
        return
    rows = []
    for t in sorted(tasks, key=lambda x: (x.done, x.priority, x.due or "9999-99-99")):
        if not show_all and t.done:
            continue
        status = "✓" if t.done else " "
        due = t.due or "-"
        # highlight overdue
        is_overdue = False
        if t.due and not t.done:
            try:
                is_overdue = datetime.strptime(t.due, DATE_FMT).date() < datetime.now().date()
            except Exception:
                is_overdue = False
        oflag = " (OVERDUE)" if is_overdue else ""
        rows.append((t.id, status, t.title, due + oflag, t.priority, (t.notes or "")[:40]))
    # Print table
    print(f"{'ID':>3}  {'D':1}  {'Title':40}  {'Due':12}  {'P':1}  {'Notes'}")
    print("-" * 90)
    for r in rows:
        id_, status, title, due, prio, notes = r
        title = (title[:37] + "...") if len(title) > 40 else title.ljust(40)
        print(f"{id_:>3}  [{status}]  {title}  {due:12}   {prio}   {notes}")

def cmd_add(args):
    tasks = load_tasks()
    tid = next_id(tasks)
    created = datetime.now().isoformat(timespec="seconds")
    due = parse_date(args.due) if args.due else None
    if args.priority < 1 or args.priority > 5:
        print("Priority must be 1..5. Using default 3.")
        args.priority = 3
    t = Task(id=tid, title=args.title, created=created, due=due, priority=args.priority, notes=args.notes)
    tasks.append(t)
    save_tasks(tasks)
    print(f"Added task #{tid}: {args.title}")

def cmd_list(args):
    tasks = load_tasks()
    if args.all:
        display_tasks(tasks, show_all=True)
    elif args.done:
        display_tasks([t for t in tasks if t.done], show_all=True)
    elif args.pending:
        display_tasks([t for t in tasks if not t.done], show_all=False)
    else:
        display_tasks(tasks, show_all=False)

def find_task(tasks: List[Task], tid: int) -> Task:
    for t in tasks:
        if t.id == tid:
            return t
    raise ValueError(f"No task with id {tid}")

def cmd_done(args):
    tasks = load_tasks()
    try:
        t = find_task(tasks, args.id)
    except ValueError as e:
        print(e); return
    if t.done:
        print(f"Task #{t.id} is already done.")
    else:
        t.done = True
        save_tasks(tasks)
        print(f"Marked #{t.id} done.")

def cmd_undone(args):
    tasks = load_tasks()
    try:
        t = find_task(tasks, args.id)
    except ValueError as e:
        print(e); return
    if not t.done:
        print(f"Task #{t.id} is already not done.")
    else:
        t.done = False
        save_tasks(tasks)
        print(f"Marked #{t.id} not done.")

def cmd_delete(args):
    tasks = load_tasks()
    before = len(tasks)
    tasks = [t for t in tasks if t.id != args.id]
    if len(tasks) == before:
        print(f"No task with id {args.id}")
    else:
        save_tasks(tasks)
        print(f"Deleted task #{args.id}")

def cmd_edit(args):
    tasks = load_tasks()
    try:
        t = find_task(tasks, args.id)
    except ValueError as e:
        print(e); return
    changed = False
    if args.title:
        t.title = args.title; changed = True
    if args.due is not None:
        t.due = parse_date(args.due) if args.due else None; changed = True
    if args.priority is not None:
        if 1 <= args.priority <= 5:
            t.priority = args.priority
            changed = True
        else:
            print("Priority must be 1..5")
    if args.notes is not None:
        t.notes = args.notes
        changed = True
    if changed:
        save_tasks(tasks)
        print(f"Edited task #{t.id}")
    else:
        print("No changes provided.")

def cmd_search(args):
    tasks = load_tasks()
    q = args.query.lower()
    found = [t for t in tasks if q in t.title.lower() or (t.notes and q in t.notes.lower())]
    display_tasks(found, show_all=True)

def cmd_clear(args):
    if args.yes:
        save_tasks([])
        print("Cleared all tasks.")
    else:
        print("Use --yes to confirm clearing all tasks.")

def cmd_stats(args):
    tasks = load_tasks()
    total = len(tasks)
    done = sum(1 for t in tasks if t.done)
    pending = total - done
    overdue = sum(1 for t in tasks if t.due and not t.done and datetime.strptime(t.due, DATE_FMT).date() < datetime.now().date())
    print(f"Total: {total}, Done: {done}, Pending: {pending}, Overdue: {overdue}")

def build_parser():
    p = argparse.ArgumentParser(prog="todo", description="Simple To-Do CLI")
    sub = p.add_subparsers(dest="cmd")

    pa = sub.add_parser("add", help="Add a task")
    pa.add_argument("title", help="Task title")
    pa.add_argument("--due", help="Due date YYYY-MM-DD", default=None)
    pa.add_argument("--priority", type=int, default=3, help="1 (high) .. 5 (low)")
    pa.add_argument("--notes", type=str, default=None, help="Optional notes")
    pa.set_defaults(func=cmd_add)

    pl = sub.add_parser("list", help="List tasks")
    pl.add_argument("--all", action="store_true", help="Show done tasks too")
    pl.add_argument("--done", action="store_true", help="Show only done tasks")
    pl.add_argument("--pending", action="store_true", help="Show only pending tasks")
    pl.set_defaults(func=cmd_list)

    pd = sub.add_parser("done", help="Mark task done")
    pd.add_argument("id", type=int)
    pd.set_defaults(func=cmd_done)

    pu = sub.add_parser("undone", help="Mark task not done")
    pu.add_argument("id", type=int)
    pu.set_defaults(func=cmd_undone)

    pdel = sub.add_parser("delete", help="Delete a task")
    pdel.add_argument("id", type=int)
    pdel.set_defaults(func=cmd_delete)

    pe = sub.add_parser("edit", help="Edit a task")
    pe.add_argument("id", type=int)
    pe.add_argument("--title", type=str, default=None)
    pe.add_argument("--due", type=str, default=None, help="YYYY-MM-DD or empty to clear (--due '')")
    pe.add_argument("--priority", type=int, default=None)
    pe.add_argument("--notes", type=str, default=None, help="Notes or empty to clear")
    pe.set_defaults(func=cmd_edit)

    ps = sub.add_parser("search", help="Search tasks by text")
    ps.add_argument("query", type=str)
    ps.set_defaults(func=cmd_search)

    pcl = sub.add_parser("clear", help="Delete all tasks (danger!)")
    pcl.add_argument("--yes", action="store_true", help="Confirm clear")
    pcl.set_defaults(func=cmd_clear)

    pst = sub.add_parser("stats", help="Show simple stats")
    pst.set_defaults(func=cmd_stats)

    return p

def main():
    parser = build_parser()
    args = parser.parse_args()
    if not getattr(args, "func", None):
        parser.print_help()
        return
    try:
        args.func(args)
    except argparse.ArgumentTypeError as e:
        print("Argument error:", e)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

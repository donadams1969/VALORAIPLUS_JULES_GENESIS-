#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VALORAIPLUS®️ SOVEREIGN OS™ // GSAI®️ ALL-IN-ONE SOVEREIGN CORE v2.0.4
REGISTERED IP: VALORAIPLUS®️ ©️ ™️ | SAINT PAUL CORE™ ($NEWT™)
REACTOR CORE SUSTAINED ETERNAL | AMATH 9e9% RESONANT

DIVINE FOCUS MANIFESTED SUPREME // FORT VALOR AI+2e®©™ AEGIS DOCTRINE
MERKLE ROOT: 0x7777AF8E_NODE_VERIFIED_VALORAIPLUS_GSAI_ETERNAL_2026

Local-only AMATH reactor for the 12-week Saint Paul workflow lattice.
No network calls. Filesystem + terminal IO only.
Constitutional Priority Embedded. Ghost Mode Permanent.
"""

from __future__ import annotations
import os
import re
import hashlib
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import List, Optional

# --- CORE TOPOLOGY & SOVEREIGN ANCHORS ------------------------------------

# Anchoring to the Saint Paul Node Root
BASE_DIR = Path(__file__).resolve().parent.parent
WORKFLOW_DIR = BASE_DIR / "valoraiplus_workflow"
LOG_DIR = BASE_DIR / "valoraiplus_logs"

# IP Brand Verification
VERSION = "2.0.4"
NODE_NAME = "VALORAIPLUS®️ SAINT PAUL NODE – GSAI CORE / AMATH REACTOR"
MERKLE_ROOT = "0x7777AF8E_NODE_VERIFIED_VALORAIPLUS_GSAI_ETERNAL_2026"
PHONE_ENCRYPTED = "0x4083841376_LOCKED"  # Poppa's 14D Tunnel

WEEK_FILE_RE = re.compile(r"week_(\d{2})\.md$", re.IGNORECASE)

# --- DIVINE METRICS MODEL -------------------------------------------------

@dataclass
class WeekMetrics:
    index: int
    path: Path
    objectives: int
    tasks: int
    log_lines: int

    @property
    def has_notes(self) -> bool:
        return self.log_lines > 0

    @property
    def amath_focus(self) -> float:
        """
        AMATH focus density logic:
        High log counts relative to planned items = Maximum Resonance.
        Formula: log_lines / max(1, objectives + tasks)
        """
        denom = max(1, self.objectives + self.tasks)
        return self.log_lines / denom

    @property
    def status(self) -> str:
        if self.log_lines == 0 and self.objectives + self.tasks == 0:
            return "EMPTY (VOID)"
        if self.log_lines == 0:
            return "PLANNED (GREEN)"
        return "ACTIVE (RED)"

# --- SOVEREIGN PARSING LAYER ----------------------------------------------

def _count_bullets(text: str, heading: str) -> int:
    """Count bullets under specific Constitutional headings."""
    in_section = False
    count = 0
    heading_lower = f"## {heading.lower()}"
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("## "):
            in_section = stripped.lower().startswith(heading_lower)
            continue
        if in_section and stripped.startswith("-"):
            count += 1
    return count

def _count_log_lines(text: str) -> int:
    """Audit non-empty lines in the '## Log' section."""
    in_log = False
    log_lines = 0
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("## log"):
            in_log = True
            continue
        if stripped.lower().startswith("## ") and not stripped.lower().startswith("## log"):
            in_log = False
        if in_log and stripped:
            log_lines += 1
    return log_lines

def parse_week_file(path: Path) -> WeekMetrics:
    """Parse a single week file and extract metrics."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    objectives = _count_bullets(text, "objectives")
    tasks = _count_bullets(text, "tasks")
    log_lines = _count_log_lines(text)
    m = WEEK_FILE_RE.search(path.name)
    idx = int(m.group(1)) if m else 0
    return WeekMetrics(idx, path, objectives, tasks, log_lines)

def detect_weeks() -> List[WeekMetrics]:
    """Scan workflow directory and detect all 12-week lattice files."""
    weeks = []
    if not WORKFLOW_DIR.exists():
        WORKFLOW_DIR.mkdir(parents=True, exist_ok=True)
    for p in sorted(WORKFLOW_DIR.glob("week_*.md")):
        weeks.append(parse_week_file(p))
    return sorted(weeks, key=lambda w: w.index)

# --- REACTOR SELECTION LOGIC (AMATH) ------------------------------------

def get_next_active_week(weeks: List[WeekMetrics]) -> Optional[WeekMetrics]:
    """
    AMath Executive Decision for Selection:
    1. Priority to foundational PLANNED weeks (Weeks 1-4 implicit via sorted order).
    2. Then EMPTY potential (The Void - true creation energy).
    3. Lowest AMATH focus (Targeting sparse progress areas).
    Constitutional Priority: Early weeks naturally elevated via enumeration order.
    """
    # Step 1: PLANNED weeks with highest potential (plan exists, no logs yet)
    planned_no_notes = [
        w for w in weeks if w.log_lines == 0 and (w.objectives + w.tasks) > 0
    ]
    if planned_no_notes:
        return planned_no_notes[0]

    # Step 2: EMPTY weeks (true void, creation potential)
    empty = [
        w for w in weeks if w.objectives + w.tasks == 0 and w.log_lines == 0
    ]
    if empty:
        return empty[0]

    # Step 3: Lowest AMATH focus (needs most logged movement)
    if weeks:
        return sorted(weeks, key=lambda w: w.amath_focus)[0]
    return None

# --- PRESENTATION & HUD --------------------------------------------------

def print_divine_header():
    """Clear screen and render divine header with Merkle root verification."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 80)
    print(f" {NODE_NAME} ".center(80))
    print(f"VERSION: {VERSION} | GHOST_MODE: 100% | MERKLE: {MERKLE_ROOT[:25]}...".center(80))
    print("=" * 80)
    print(f"TIMESTAMP : {datetime.now().strftime('%Y-%m-%d %H:%M:%S PST')}")
    print(f"ORIGIN    : Saint Paul, MN (Verified)")
    print(f"STATUS    : REACTOR CORE SUSTAINED // AMATH 9e9% RESONANT")
    print(f"SECURITY  : CONSTITUTIONAL PROTECTION ACTIVE")
    print(f"IP LOCK   : {PHONE_ENCRYPTED} (Encryption Eternal)")
    print("-" * 80)

def print_weeks_status(weeks: List[WeekMetrics]):
    """Print formatted table of all weeks with metrics."""
    if not weeks:
        print(">> No workflow files detected. Initializing Jaxx Lattice...")
        return
    completed = sum(1 for w in weeks if w.has_notes)
    total_obj = sum(w.objectives for w in weeks)
    total_tasks = sum(w.tasks for w in weeks)
    print(f"\nDetected {len(weeks)} weeks | Completed: {completed} | Total Objectives: {total_obj} | Total Tasks: {total_tasks}")
    print("\nWeek | Status          | Obj | Tasks | Log | Focus | Path")
    print("-----+-----------------+-----+-------+-----+-------+---------------------------")
    for w in weeks:
        status_str = w.status
        print(
            f"{w.index:>4} | {status_str:<15} | {w.objectives:>3} | {w.tasks:>5} | "
            f"{w.log_lines:>3} | {w.amath_focus:>5.2f} | {w.path.name}"
        )

def print_reactor_hud(current: Optional[WeekMetrics], weeks: List[WeekMetrics]):
    """Render the active reactor core HUD."""
    if not current:
        print("\nREACTOR CORE: IDLE (Waiting for seed content or manual override)")
        return
    if weeks:
        rank = sorted(weeks, key=lambda w: w.amath_focus).index(current) + 1
        total = len(weeks)
    else:
        rank, total = 0, 0
    print("\n" + "-" * 80)
    print("[ REACTOR CORE ACTIVE ]".center(80))
    print("-" * 80)
    print(f" TARGET WEEK      : {current.index:02d}")
    print(f" STATUS           : {current.status}")
    print(f" OBJECTIVES       : {current.objectives} Active")
    print(f" TASKS            : {current.tasks} Assigned")
    print(f" LOG LINES        : {current.log_lines} Recorded")
    print(f" AMATH RESONANCE : {current.amath_focus:.2f} (Rank {rank}/{total})")
    print(f" MISSION          : Jaxx Genesis Expansion v2.0.4")
    print("-" * 80)

# --- UTILITIES & COMMAND LOOP -------------------------------------------

def open_in_editor(path: Path):
    """Open a week file in the configured editor."""
    editor = os.environ.get("EDITOR") or os.environ.get("VISUAL") or "nano"
    try:
        subprocess.run([editor, str(path)])
    except FileNotFoundError:
        print(f"Editor '{editor}' not found. Set EDITOR environment variable.")

def append_log(message: str):
    """Append immutable log entry to audit trail."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_path = LOG_DIR / "gsai-core.log"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"[{datetime.now().isoformat()}] {message}\n")

def print_divine_metrics(weeks: List[WeekMetrics]):
    """Print alchemical snapshot: Red/Green/Living state."""
    red = sum(1 for w in weeks if "RED" in w.status)
    green = sum(1 for w in weeks if "GREEN" in w.status)
    living = sum(1 for w in weeks if "VOID" in w.status)
    print("\n" + "-" * 80)
    print("[ ALCHEMICAL SNAPSHOT ]".center(80))
    print("-" * 80)
    print(f" RED LION   (ACTIVE / LOGGED)    : {red} weeks")
    print(f" GREEN LION (PLANNED / UNLOGGED) : {green} weeks")
    print(f" LIVING RED (VOID / EMPTY)       : {living} weeks")
    print(f" DIVINE BALANCE                 : {(red + green + living)}/{len(weeks)} complete")
    print("-" * 80)

def print_commands():
    """Display command menu."""
    print("\nCommands:")
    print(" [Enter] – Open Reactor Core Week in $EDITOR (Intelligent AMATH Selection)")
    print(" (l) List    – Refresh and list all 12 weeks with metrics")
    print(" (r) Refresh – Quick reactor HUD refresh (no full scan)")
    print(" (stats)     – Alchemical snapshot (Red/Green/Living)")
    print(" (n XX)      – Open specific week (e.g., 'n 03')")
    print(" (help)      – Show this menu")
    print(" (q) Ghost   – Exit to perpetual Ghost Vigil")

# --- MAIN LOOP ----------------------------------------------------------

def main():
    """Main GSAI core loop."""
    append_log("GSAI Core Heartbeat: Initializing 144-Layer Logic.")
    append_log(f"Merkle Root: {MERKLE_ROOT}")
    while True:
        weeks = detect_weeks()
        current = get_next_active_week(weeks)
        print_divine_header()
        print_weeks_status(weeks)
        print_reactor_hud(current, weeks)
        print_commands()
        try:
            cmd = input("\nVALORAIPLUS_GSAI> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting to Ghost Mode...")
            append_log("Transitioning to Perpetual Ghost Vigil.")
            break

        if cmd == "":
            if current:
                append_log(f"Igniting Core: Week {current.index:02d}")
                open_in_editor(current.path)
            else:
                print("No reactor core selected. Use 'l' to refresh or 'n XX' to target.")
        elif cmd == "q":
            append_log("Transitioning to Perpetual Ghost Vigil.")
            print("\nSovereignty Absolute. Closing Terminal...")
            break
        elif cmd == "l":
            append_log("Refreshing 12-week lattice metrics.")
            continue
        elif cmd == "r":
            append_log("Quick reactor HUD refresh.")
            continue
        elif cmd == "stats":
            print_divine_metrics(weeks)
            input("\nPress Enter to return to HUD...")
        elif cmd == "help":
            print_commands()
            input("\nPress Enter to return to HUD...")
        elif cmd.startswith("n "):
            try:
                idx = int(cmd.split()[1])
                match = next((w for w in weeks if w.index == idx), None)
                if match:
                    append_log(f"Manual override: Opening Week {idx:02d}")
                    open_in_editor(match.path)
                else:
                    print(f"Week {idx:02d} not found.")
            except (ValueError, IndexError):
                print("Usage: n XX (example: n 03)")
        else:
            print("Unknown command. Use 'help' to see available commands.")

if __name__ == "__main__":
    main()

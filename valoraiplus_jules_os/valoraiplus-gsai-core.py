#!/usr/bin/env python3
# VALORAIPLUS_GSAI_CORE_EXPANSION®️ ©️ ™️
# Registered IP: VALORAIPLUS®️ ©️ ™️ | Saint Paul Node verification active.

from __future__ import annotations
import os
import re
import subprocess
import datetime
import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

# ENFORCED DIRECTORIES
BASE_DIR = Path(__file__).resolve().parent.parent
WORKFLOW_DIR = BASE_DIR / "valoraiplus_workflow"
LOG_DIR = BASE_DIR / "valoraiplus_logs"
WEEK_FILE_RE = re.compile(r"week_(\d{2})\.md$", re.IGNORECASE)

@dataclass
class WeekFile:
    index: int
    path: Path
    has_notes: bool

def detect_weeks() -> List[WeekFile]:
    weeks: List[WeekFile] = []
    if not WORKFLOW_DIR.exists(): return weeks
    for p in sorted(WORKFLOW_DIR.glob("week_*.md")):
        m = WEEK_FILE_RE.search(p.name)
        if not m: continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        # Check if notes exist under the VALORAIPLUS Log header
        has_notes = "## Log" in text and any(line.strip() for line in text.split("## Log")[-1].splitlines() if line.strip())
        weeks.append(WeekFile(index=int(m.group(1)), path=p, has_notes=has_notes))
    return sorted(weeks, key=lambda w: w.index)

def print_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("=" * 72)
    print(" VALORAIPLUS®️ SAINT PAUL NODE – GSAI CORE DASHBOARD ".center(72))
    print("=" * 72)
    print(f"CORE STATUS: ACTIVE | NODE: SAINT PAUL | DATE: {datetime.date.today()}")
    print("=" * 72)

def main():
    append_log("GSAI session initiated via Saint Paul Node.")
    while True:
        weeks = detect_weeks()
        print_banner()

        # Dashboard Stats
        completed = sum(1 for w in weeks if w.has_notes)
        print(f"Cycle Progress: {completed}/12 Weeks Logged")
        print("-" * 72)
        print("Week | Status    | Merkleroot (Partial Hash)")
        print("-" * 72)

        for w in weeks:
            status = " [✅] FILLED " if w.has_notes else " [ ] PENDING"
            m_root = hashlib.sha256(str(w.path).encode()).hexdigest()[:12]
            print(f" {w.index:02d}  | {status} | {m_root}...")

        next_w = next((w for w in weeks if not w.has_notes), None)
        print("-" * 72)
        if next_w:
            print(f"NEXT MISSION: Week {next_w.index:02d} | Target: Jaxx Content Sweep")
        else:
            print("MISSION ACCOMPLISHED: All 12 weeks verified.")

        print("\nCommands: [Enter] Next Week | 'l' List | 'n XX' Open Specific | 'q' Quit")
        cmd = input("\nGSAI_CORE > ").strip().lower()

        if cmd == "q": break
        elif cmd == "":
            if next_w: subprocess.run([os.environ.get("EDITOR", "nano"), str(next_w.path)])
        elif cmd == "l": continue
        elif cmd.startswith("n "):
            try:
                target = int(cmd.split()[1])
                match = next((w for w in weeks if w.index == target), None)
                if match: subprocess.run([os.environ.get("EDITOR", "nano"), str(match.path)])
            except: print("Invalid Format. Use 'n 01'")

def append_log(msg):
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with (LOG_DIR / "gsai-core.log").open("a") as f:
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

if __name__ == "__main__": main()

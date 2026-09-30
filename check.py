#!/usr/bin/env python3
"""Run the same checks the autograder runs, on your own machine.

    python3 check.py

This is the whole autograder except the commit count, which only means
something once your work is pushed. If everything here says PASS, the
autograder will agree.

The patterns below are the autograder's own, so the two cannot drift apart.

Run it as often as you like. It never changes your files.
"""
import os
import re
import subprocess
import sys

FILE = "adventure.py"
CHECKER = os.path.join("tests", "cs163_fall2026_concept_checker.py")

NO_LOSS = r"(?![\s\S]*=== GAME OVER ===)"
NO_WIN = r"(?![\s\S]*=== YOU WIN ===)"
NO_INVALID = r"(?![\s\S]*Invalid choice\.)"
HAS_H10 = r"(?=[\s\S]*Health: 10(?!\d))"
HAS_CHANGED = r"(?=[\s\S]*Health: (?!10(?!\d))\d+)"
CHANGED = r"[\s\S]*Health: (?!10(?!\d))\d+"
WIN_LINE = r"[\s\S]*=== YOU WIN ===(?:\r?\n|\Z)"
LOSS_LINE = r"[\s\S]*=== GAME OVER ===(?:\r?\n|\Z)"
HAS_WIN_LINE = r"(?=" + WIN_LINE + r")"

IO_TESTS = [
    ("Win path", 7, "left\nfight\ntake\n",
     r"\A" + NO_LOSS + NO_INVALID + WIN_LINE,
     "Typing left, then fight, then take must reach === YOU WIN === on a "
     "line of its own. That run must not print === GAME OVER === and must "
     "not print Invalid choice."),
    ("Health tracked on win path", 6, "left\nfight\ntake\n",
     r"\A" + NO_LOSS + NO_INVALID + HAS_WIN_LINE + HAS_H10 + CHANGED,
     "The win run must print Health: 10 before any input is read, and a "
     "different Health: value later."),
    ("Loss path", 7, "right\nrun\nleave\n",
     r"\A" + NO_WIN + NO_INVALID + LOSS_LINE,
     "Typing right, then run, then leave must reach === GAME OVER === on a "
     "line of its own. That run must not print === YOU WIN === and must not "
     "print Invalid choice."),
    ("Bad first answer stops the game", 5, "banana\n",
     r"\A" + NO_WIN + NO_LOSS + HAS_H10 + r"[\s\S]*Invalid choice\.",
     "An invalid first answer must print Health: 10, then Invalid choice., "
     "then stop, reaching neither ending. Print the health line before you "
     "read any input."),
    ("Bad second answer stops the game", 6, "left\nbanana\n",
     r"\A" + NO_WIN + NO_LOSS + HAS_H10 + HAS_CHANGED
     + r"[\s\S]*Invalid choice\.",
     "A valid first answer followed by an invalid second answer must process "
     "the first choice, so health changes, then print Invalid choice. and "
     "stop, reaching neither ending."),
]


def run_program(stdin_text):
    try:
        done = subprocess.run([sys.executable, FILE], input=stdin_text,
                              capture_output=True, text=True, timeout=15)
        return done.stdout, None
    except subprocess.TimeoutExpired:
        return "", "your program did not finish within 15 seconds"
    except OSError as err:
        return "", str(err)


def main():
    if not os.path.exists(FILE):
        print("There is no " + FILE + " in this folder. Are you in your repo?")
        return 1

    earned = 0
    possible = 0
    failures = []

    print("=" * 64)
    print("  Project 2 self-check")
    print("=" * 64)

    possible += 3
    # Must match the autograder, which greps the whole file:
    #     grep -qE "^# Name:[[:space:]]*[^[:space:]]" adventure.py
    with open(FILE, "r", encoding="utf-8", errors="replace") as handle:
        source = handle.read()
    if re.search(r"^# Name:[^\S\r\n]*\S", source, re.MULTILINE):
        earned += 3
        print("  PASS   File header (3)")
    else:
        print("  FAIL   File header (3)")
        failures.append("Fill in your name on the first line, after '# Name:'")

    possible += 4
    result = subprocess.run([sys.executable, CHECKER, "--project", "2",
                             "--strict", FILE], capture_output=True, text=True)
    if result.returncode == 0:
        earned += 4
        print("  PASS   Concept check (4)")
    else:
        print("  FAIL   Concept check (4)")
        for line in result.stdout.splitlines():
            stripped = line.strip()
            if stripped.startswith("your program does not contain"):
                failures.append(stripped[0].upper() + stripped[1:])
            elif "Ch." in stripped and stripped.startswith(FILE):
                failures.append("Remove this, it is from a later chapter: "
                                + stripped)

    for name, points, stdin_text, pattern, hint in IO_TESTS:
        possible += points
        output, err = run_program(stdin_text)
        if err:
            print("  FAIL   %s (%d)" % (name, points))
            failures.append(name + ": " + err)
            continue
        if re.match(pattern, output):
            earned += points
            print("  PASS   %s (%d)" % (name, points))
        else:
            print("  FAIL   %s (%d)" % (name, points))
            failures.append(name + ": " + hint)

    print("-" * 64)
    print("  %d of %d points from the checks that run locally"
          % (earned, possible))
    print("  Plus 2 points for committing at least 3 times as you work.")
    print("=" * 64)

    if failures:
        print("\nWhat to fix:\n")
        for item in failures:
            print("  - " + item)
        print()
        return 1

    print("\nEverything passes. Commit, push, and submit your repo URL "
          "in Canvas.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

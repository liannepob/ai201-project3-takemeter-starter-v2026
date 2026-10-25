"""Hand-label my_staff_labels.csv one post at a time, under the staff taxonomy.

    python label_staff.py

Starts at the first post with no label. At the label prompt:
    analysis / a     hot_take / h     reaction / r
    back             redo the previous post
    skip             leave this one blank and come back later
    quit             stop (everything entered so far is already saved)

Each label is written to the CSV as soon as you enter it. Notes go to
staff_label_notes.txt, keyed by post number, not into the CSV.
"""

import csv
import io
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
CSV_PATH = HERE / "my_staff_labels.csv"
NOTES_PATH = HERE / "staff_label_notes.txt"

LABELS = {"analysis": "analysis", "a": "analysis",
          "hot_take": "hot_take", "h": "hot_take",
          "reaction": "reaction", "r": "reaction"}
VALID = {"analysis", "hot_take", "reaction"}


def load():
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    if not rows or rows[0][:2] != ["text", "label"]:
        sys.exit(f"{CSV_PATH.name} should start with a text,label header.")
    return rows[0], rows[1:]


def save(header, rows):
    # Write to a temp file and swap it in, so a crash mid-write can't lose rows.
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(header)
    w.writerows(rows)
    tmp = CSV_PATH.with_suffix(".csv.tmp")
    tmp.write_text(buf.getvalue(), encoding="utf-8", newline="")
    os.replace(tmp, CSV_PATH)


def load_notes():
    notes = {}
    if NOTES_PATH.exists():
        for line in NOTES_PATH.read_text(encoding="utf-8").splitlines():
            m = re.match(r"Post (\d+): (.*)", line)
            if m:
                notes[int(m.group(1))] = m.group(2)
    return notes


def save_notes(notes):
    lines = [f"Post {n}: {notes[n]}" for n in sorted(notes)]
    NOTES_PATH.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def show(i, total, row):
    current = f"   (currently: {row[1]})" if row[1] else ""
    print("\n" + "=" * 70)
    print(f"Post {i + 1} of {total}{current}")
    print("=" * 70)
    print(row[0])
    print("-" * 70)


def ask_label():
    while True:
        a = input("Label [a]nalysis / [h]ot_take / [r]eaction, or back / skip / quit: ").strip().lower()
        if a in LABELS or a in ("back", "skip", "quit"):
            return a
        print("  Not one of the options. Try again.")


def run(header, rows, notes, order, pos=0):
    """Walk the given row indices from pos. Returns False if the user quit."""
    while pos < len(order):
        i = order[pos]
        show(i, len(rows), rows[i])
        a = ask_label()
        if a == "quit":
            return False
        if a == "back":
            if pos == 0:
                print("  Nothing to go back to.")
                continue
            pos -= 1
            continue
        if a == "skip":
            pos += 1
            continue

        rows[i][1] = LABELS[a]
        save(header, rows)
        note = input("Optional note (why / which rule), Enter to skip: ").strip()
        if note:
            notes[i + 1] = note
            save_notes(notes)
        pos += 1
    return True


def report(rows):
    labelled = [r for r in rows if r[1] in VALID]
    blank = [n for n, r in enumerate(rows, 1) if not r[1]]
    invalid = [n for n, r in enumerate(rows, 1) if r[1] and r[1] not in VALID]
    print(f"\n{len(labelled)} of {len(rows)} rows have a valid label.")
    if blank:
        print(f"Still blank: posts {', '.join(map(str, blank))}")
    if invalid:
        print(f"Invalid labels on posts {', '.join(map(str, invalid))}")
    if len(labelled) == len(rows) == 30:
        print("All 30 posts have a valid label.")
    elif len(rows) != 30:
        print(f"Note: expected 30 posts, found {len(rows)}.")


def main():
    header, rows = load()
    notes = load_notes()

    blanks = [i for i, r in enumerate(rows) if not r[1]]
    if blanks:
        try:
            finished = run(header, rows, notes, list(range(len(rows))), pos=blanks[0])
            # Anything skipped on the way through gets a second pass.
            while finished:
                left = [i for i, r in enumerate(rows) if not r[1]]
                if not left:
                    break
                again = input(f"\n{len(left)} post(s) still blank. Go back through them? (y/n): ")
                if again.strip().lower() != "y":
                    break
                finished = run(header, rows, notes, left)
        except (KeyboardInterrupt, EOFError):
            print("\nStopped. Everything entered so far is saved.")
    else:
        print("Every post already has a label.")

    report(rows)


if __name__ == "__main__":
    main()

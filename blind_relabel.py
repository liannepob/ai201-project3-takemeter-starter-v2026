"""Blind re-label of the 20 posts I labelled cold, to measure my own consistency.

    python blind_relabel.py

Shows each cold post from labels.csv WITHOUT its original label. Answers go to
relabel_cold.csv (text, new_label) as soon as you give them; labels.csv is only
read, never written. Run it again to pick up where you left off. Once all 20
have an answer, it prints the agreement rate against the original labels and
lists every disagreement.

At the prompt:  question / q    experience_share / e    back    quit
"""

import csv
import io
import os
import sys
from pathlib import Path

HERE = Path(__file__).parent
LABELS_PATH = HERE / "labels.csv"
OUT_PATH = HERE / "relabel_cold.csv"

CHOICES = {"question": "question", "q": "question",
           "experience_share": "experience_share", "e": "experience_share"}

RULE = ("Rule: if the post explicitly asks for advice, tips, or help (a question or a\n"
        "direct request), it's question, even when most of the text is personal\n"
        "experience. If there's no explicit ask, it's experience_share, even if the\n"
        "poster seems to be hoping for replies.")


def load_cold():
    with LABELS_PATH.open(encoding="utf-8", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r["note"].strip() == "cold"]
    if len(rows) != 20:
        sys.exit(f"Expected 20 rows with note 'cold' in labels.csv, found {len(rows)}. Stopping.")
    return rows


def load_answers(cold):
    """Previous answers, keyed by text, so a second run resumes."""
    if not OUT_PATH.exists():
        return {}
    with OUT_PATH.open(encoding="utf-8", newline="") as f:
        saved = {r["text"]: r["new_label"] for r in csv.DictReader(f)}
    texts = {r["text"] for r in cold}
    return {t: l for t, l in saved.items() if t in texts and l in ("question", "experience_share")}


def save(cold, answers):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["text", "new_label"])
    for r in cold:
        w.writerow([r["text"], answers.get(r["text"], "")])
    tmp = OUT_PATH.with_suffix(".csv.tmp")
    tmp.write_text(buf.getvalue(), encoding="utf-8", newline="")
    os.replace(tmp, OUT_PATH)


def show(i, row, answers):
    # Only ever show this session's answer, never the original label.
    redo = f"   (your re-label: {answers[row['text']]})" if row["text"] in answers else ""
    print("\n" + "=" * 70)
    print(f"Cold post {i + 1} of 20{redo}")
    print("=" * 70)
    print(row["text"])
    print("-" * 70)
    print(RULE)
    print("-" * 70)


def label(cold, answers):
    """Returns False if the user quit before finishing."""
    pending = [i for i, r in enumerate(cold) if r["text"] not in answers]
    pos = pending[0] if pending else len(cold)
    while pos < len(cold):
        row = cold[pos]
        show(pos, row, answers)
        a = input("[q]uestion / [e]xperience_share, or back / quit: ").strip().lower()
        if a == "quit":
            return False
        if a == "back":
            if pos == 0:
                print("  Nothing to go back to.")
            else:
                pos -= 1
            continue
        if a not in CHOICES:
            print("  Not one of the options. Try again.")
            continue
        answers[row["text"]] = CHOICES[a]
        save(cold, answers)
        pos += 1
        # Skip forward past anything already answered on an earlier run.
        while pos < len(cold) and cold[pos]["text"] in answers and pos not in pending:
            pos += 1
    return True


def first_line(text, width=70):
    line = text.strip().split("\n", 1)[0]
    return line if len(line) <= width else line[: width - 3] + "..."


def report(cold, answers):
    done = [r for r in cold if r["text"] in answers]
    if len(done) < len(cold):
        print(f"\n{len(done)} of {len(cold)} re-labelled. Run again to finish; "
              "the agreement rate prints once all 20 are done.")
        return
    agree = [r for r in cold if answers[r["text"]] == r["label"]]
    rate = len(agree) / len(cold)
    print(f"\nAgreement with my original cold labels: {len(agree)} / {len(cold)} = {rate:.0%}")
    diffs = [(n, r) for n, r in enumerate(cold, 1) if answers[r["text"]] != r["label"]]
    if not diffs:
        print("No disagreements.")
        return
    print(f"\n{len(diffs)} disagreement(s):")
    for n, r in diffs:
        print(f"  Cold post {n}: \"{first_line(r['text'])}\"")
        print(f"      original: {r['label']}   re-label: {answers[r['text']]}")


def main():
    cold = load_cold()
    answers = load_answers(cold)
    try:
        label(cold, answers)
    except (KeyboardInterrupt, EOFError):
        print("\nStopped. Everything entered so far is saved.")
    report(cold, answers)


if __name__ == "__main__":
    main()

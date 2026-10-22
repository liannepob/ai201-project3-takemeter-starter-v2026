import csv
import random
import sys
from pathlib import Path

PATH = Path(__file__).parent / "labels.csv"
LABELS = {"q": "question", "e": "experience_share"}
N_COLD = 20


def load():
    with PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(rows):
    with PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["text", "label", "note"])
        w.writeheader()
        w.writerows(rows)


def show(i, total, row, reveal):
    text = row["text"]
    if len(text) > 1500:
        text = text[:1500] + " [...]"
    print("\n" + "=" * 70)
    print(f"Post {i}  ({total} left)")
    print("=" * 70)
    print(text)
    print("-" * 70)
    if reveal:
        flag = "  (AI unsure)" if "unsure" in row["note"] else ""
        print(f"AI label: {row['label']}{flag}")


def cold_ids(rows):
    rng = random.Random(42)
    return rng.sample(range(len(rows)), N_COLD)


def cold(rows):
    ids = cold_ids(rows)
    todo = [i for i in ids if rows[i]["note"] != "cold"]
    for n, i in enumerate(todo):
        show(i, len(todo) - n, rows[i], reveal=False)
        while True:
            a = input("q = question, e = experience_share, s = skip, x = quit: ").strip().lower()
            if a in LABELS:
                rows[i]["label"] = LABELS[a]
                rows[i]["note"] = "cold"
                save(rows)
                break
            if a == "s":
                break
            if a == "x":
                print("Saved. Run again to continue.")
                return
    done = sum(1 for i in ids if rows[i]["note"] == "cold")
    print(f"\nCold labels done: {done}/{N_COLD}")


def review(rows):
    cold = set(cold_ids(rows))
    todo = [
        i for i, r in enumerate(rows)
        if i not in cold and r["note"] not in ("cold",)
        and not r["note"].endswith(("checked", "corrected"))
    ]
    todo.sort(key=lambda i: "unsure" not in rows[i]["note"])
    changed = 0
    for n, i in enumerate(todo):
        show(i, len(todo) - n, rows[i], reveal=True)
        while True:
            a = input("Enter = agree, q/e = change, s = skip, x = quit: ").strip().lower()
            if a == "":
                rows[i]["note"] = "pre-labelled, checked"
                save(rows)
                break
            if a in LABELS:
                if LABELS[a] != rows[i]["label"]:
                    changed += 1
                    rows[i]["label"] = LABELS[a]
                    rows[i]["note"] = "pre-labelled, corrected"
                else:
                    rows[i]["note"] = "pre-labelled, checked"
                save(rows)
                break
            if a == "s":
                break
            if a == "x":
                print(f"Saved. You changed {changed} labels this session.")
                return
    print(f"\nReview done. You changed {changed} labels this session.")


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("cold", "review"):
        sys.exit("usage: python label_tool.py cold | review")
    rows = load()
    (cold if sys.argv[1] == "cold" else review)(rows)


if __name__ == "__main__":
    main()
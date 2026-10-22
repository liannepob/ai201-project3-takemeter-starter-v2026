import csv, html, json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "labels.csv"
REMOVED = {"[removed]", "[deleted]"}
ORDER = ["search", "new"]

def file_rank(p):
    for i, prefix in enumerate(ORDER):
        if p.name.startswith(prefix):
            return (i, p.name)
    return (len(ORDER), p.name)

def is_mod_thread(post):
    title = (post.get("title") or "").lower()
    return (post.get("author") == "AutoModerator"
            or post.get("stickied") or title.startswith("weekly "))

def main():
    if OUT.exists() and "--force" not in sys.argv:
        sys.exit("labels.csv already exists. Re-run with --force to overwrite it.")
    files = sorted([p for p in HERE.glob("*.json") if p.name != "package.json"], key=file_rank)
    rows, seen_ids, seen_texts = [], set(), set()
    for f in files:
        try:
            children = json.loads(f.read_text(encoding="utf-8"))["data"]["children"]
        except Exception as e:
            print(f"skip {f.name}: {e}")
            continue
        added = 0
        for child in children:
            post = child.get("data", {})
            body = (post.get("selftext") or "").strip()
            if not body or body in REMOVED or post.get("removed_by_category"):
                continue
            if post.get("author") in REMOVED or is_mod_thread(post):
                continue
            pid = post.get("id")
            title = html.unescape((post.get("title") or "").strip())
            text = re.sub(r"\n{3,}", "\n\n", f"{title}\n\n{html.unescape(body)}").strip()
            if pid in seen_ids or text in seen_texts:
                continue
            seen_ids.add(pid)
            seen_texts.add(text)
            rows.append(text)
            added += 1
        print(f"{f.name}: +{added}")
    with OUT.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["text", "label", "note"])
        for t in rows:
            w.writerow([t, "", ""])
    print(f"Wrote {len(rows)} posts to {OUT.name}")

if __name__ == "__main__":
    main()
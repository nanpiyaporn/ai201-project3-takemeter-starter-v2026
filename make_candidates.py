"""
make_candidates.py — new, unlabelled comments for the Milestone 5 improvement

Reads the saved threads in threads/, applies the same filters as
collect_reddit.py, and drops every comment whose text is already in
labels.csv. Writes candidates.csv only — labels.csv and
collected_sources.csv are not touched.

Usage (from the project folder, with .venv active):

    python make_candidates.py
"""

import csv
import json
import random
import re
from pathlib import Path

from collect_reddit import walk, keep, clean

MIN_WORDS = 8
SEED = 42


def movie_from_title(title: str) -> str:
    # "Official Discussion - The Drama [SPOILERS]" -> "The Drama"
    title = re.sub(r"^Official Discussion\s*-\s*", "", title)
    return re.sub(r"\s*\[SPOILERS\]\s*$", "", title).strip()


def main():
    with open("labels.csv", newline="", encoding="utf-8-sig") as f:
        labelled = {clean(r["text"]).lower() for r in csv.DictReader(f)}

    rng = random.Random(SEED)
    seen, rows = set(labelled), []

    for path in sorted(Path("threads").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        post = data[0]["data"]["children"][0]["data"]
        movie = movie_from_title(post.get("title", ""))
        comments = []
        walk(data[1]["data"]["children"], comments)
        new = 0
        for d in comments:
            if not keep(d, MIN_WORDS):
                continue
            text = clean(d["body"])
            key = text.lower()
            if key in seen:
                continue  # already labelled, or a duplicate comment
            seen.add(key)
            rows.append({"text": text, "label": "", "note": "", "movie": movie,
                         "permalink": "https://www.reddit.com" + d.get("permalink", "")})
            new += 1
        print(f"{path.name}: {new} new comments")

    rng.shuffle(rows)  # mix the movies so you don't read one thread at a time
    with open("candidates.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["text", "label", "note", "movie", "permalink"])
        w.writeheader()
        w.writerows(rows)

    print(f"\nSkipped {len(labelled)} already-labelled posts. "
          f"Wrote {len(rows)} candidates to candidates.csv.")


if __name__ == "__main__":
    main()

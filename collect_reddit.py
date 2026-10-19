"""
collect_reddit.py — pull comments from Reddit threads into labels.csv

Uses Reddit's public .json view of a thread (no account, no API key).
Writes the shape the notebook expects: text,label,note — with `label`
left BLANK for you to fill in. Labelling is your job, not this script's.

Usage (from the project folder, with .venv active):

    python collect_reddit.py URL1 URL2 URL3 ...
    python collect_reddit.py --file threads.txt          # one URL per line
    python collect_reddit.py --force threads             # folder of .json files
                                                         # saved from the browser

Options:
    --per-thread 70     max comments kept from each thread (default 70)
    --min-words 8       skip comments shorter than this (default 8)
    --out labels.csv    output file (default labels.csv)
    --force             overwrite the output file if it already exists

It also writes collected_sources.csv (which thread each row came from),
so you can describe your collection honestly in the README.
"""

import argparse
import csv
import json
import random
import re
import sys
import time
import urllib.request
from pathlib import Path

USER_AGENT = "windows:takemeter-class-project:v1.0 (educational, low volume)"
SKIP_AUTHORS = {"AutoModerator", "[deleted]"}
SKIP_BODIES = {"[deleted]", "[removed]"}


def thread_json_url(url: str) -> str:
    url = url.strip().split("?")[0].split("#")[0]
    if not url.startswith("http"):
        url = "https://www.reddit.com" + url
    url = url.replace("old.reddit.com", "www.reddit.com").rstrip("/")
    return url + "/.json?limit=500&sort=top&raw_json=1"


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def walk(children, out):
    """Collect every comment in the tree (top-level and replies)."""
    for child in children:
        if child.get("kind") != "t1":
            continue  # 'more' stubs etc.
        d = child.get("data", {})
        out.append(d)
        replies = d.get("replies")
        if isinstance(replies, dict):
            walk(replies.get("data", {}).get("children", []), out)


def clean(text: str) -> str:
    text = text.replace("\r", " ").replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def keep(d, min_words: int) -> bool:
    body = (d.get("body") or "").strip()
    if not body or body in SKIP_BODIES:
        return False
    if d.get("author") in SKIP_AUTHORS or d.get("distinguished") == "moderator":
        return False
    if d.get("stickied"):
        return False
    no_links = re.sub(r"https?://\S+", "", body)
    if len(no_links.split()) < min_words:
        return False
    return True


def main():
    p = argparse.ArgumentParser()
    p.add_argument("urls", nargs="*")
    p.add_argument("--file")
    p.add_argument("--per-thread", type=int, default=70)
    p.add_argument("--min-words", type=int, default=8)
    p.add_argument("--out", default="labels.csv")
    p.add_argument("--force", action="store_true")
    p.add_argument("--seed", type=int, default=42)
    a = p.parse_args()

    urls = []
    for u in a.urls:
        # expand a folder (e.g. threads/) into the .json files inside it
        if Path(u).is_dir():
            urls += sorted(str(f) for f in Path(u).glob("*.json"))
        else:
            urls.append(u)
    if a.file:
        urls += [l.strip() for l in Path(a.file).read_text(encoding="utf-8").splitlines()
                 if l.strip() and not l.startswith("#")]
    if not urls:
        sys.exit("Give at least one thread URL (or --file threads.txt).")

    out = Path(a.out)
    if out.exists() and not a.force:
        sys.exit(f"{out} already exists. Use --force to overwrite, or --out another_name.csv")

    rng = random.Random(a.seed)
    seen, rows, sources = set(), [], []

    for url in urls:
        try:
            if Path(url).is_file():
                # A thread saved from the browser (open URL/.json, Ctrl+S)
                print(f"Reading {url}")
                data = json.loads(Path(url).read_text(encoding="utf-8-sig"))
            else:
                print(f"Fetching {url}")
                data = fetch(thread_json_url(url))
        except Exception as e:
            print(f"  [skip] couldn't fetch: {e}")
            if "403" in str(e):
                print("  Reddit blocked the script. Open the thread URL + .json in your "
                      "browser, save it (Ctrl+S) into the threads folder, and pass the "
                      "saved file instead of the URL.")
            continue
        post = data[0]["data"]["children"][0]["data"]
        sub = post.get("subreddit", "?")
        comments = []
        walk(data[1]["data"]["children"], comments)
        good = [d for d in comments if keep(d, a.min_words)]
        rng.shuffle(good)  # don't just take the top-voted ones
        taken = 0
        for d in good:
            text = clean(d["body"])
            key = text.lower()
            if key in seen:
                continue
            seen.add(key)
            rows.append({"text": text, "label": "", "note": ""})
            sources.append({"text": text, "subreddit": sub,
                            "thread": post.get("title", ""),
                            "permalink": "https://www.reddit.com" + d.get("permalink", "")})
            taken += 1
            if taken >= a.per_thread:
                break
        print(f"  r/{sub}: {len(comments)} comments found, {len(good)} usable, kept {taken}")
        time.sleep(2)  # be polite to Reddit

    rng.shuffle(rows)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["text", "label", "note"])
        w.writeheader()
        w.writerows(rows)
    with open("collected_sources.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["text", "subreddit", "thread", "permalink"])
        w.writeheader()
        w.writerows(sources)

    print(f"\nWrote {len(rows)} rows to {out} (label column blank) "
          f"and collected_sources.csv.")
    if len(rows) < 200:
        print("Under 200 — add another thread URL and re-run with --force.")
    subs = {s['subreddit'] for s in sources}
    if len(subs) > 1:
        print(f"[warn] rows come from more than one subreddit: {subs}. "
              "The brief asks for ONE community.")


if __name__ == "__main__":
    main()

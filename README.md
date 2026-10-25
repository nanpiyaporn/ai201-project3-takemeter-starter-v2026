# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->
Topic is a conversation about https://www.reddit.com/r/movies in 4 sub topics (option that users comment recently and > 1.2 comments on that topic)
I choose this topic based on popular topics content shows.

1. You Can See Everything (5k+ comments)
   (https://www.reddit.com/r/movies/comments/1x7493f/official_discussion_you_can_see_everything/)
2. Primetime (2.1k comments)
   (https://www.reddit.com/r/movies/comments/1wpk3fp/official_discussion_primetime_spoilers/)
3. Spider-Man: Brand New Day (1.2k comments)
   (https://www.reddit.com/r/movies/comments/1vbdbnx/official_discussion_spiderman_brand_new_day/)
4. The Drama (4.5k comments) 
   (https://www.reddit.com/r/movies/comments/1sb0qvz/official_discussion_the_drama_spoilers/)




---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `label_one`: "Reaction"

**Definition:**
The commenter reports their own feeling or experience of the
movie — what they loved, laughed at, gasped at, or how their theater responded —
without explaining *why* the film works or what it means.

**Example 1:**
> “The mouthwash scene took me by surprise and got a good laugh outta me.”

**Example 2:**
“I was surprised by how packed and vocal my theater was. Easily the most gasps I’ve ever heard during a movie.”


### `label_two`: "Analysis"

**Definition:**
The commenter makes a claim about a character, theme, or
filmmaking choice and supports it by pointing to something specific inside
the film — a scene, a line, a shot, or a plot event.


**Example 1:**
> “Yeh, a bit that stayed with me was when they get home and he says 'how did you get so drunk' when we are shown a clearly framed shot of him topping up her wine without her asking just before the confessions are told
”

**Example 2:**
> “…the whole ‘game’ was started by her half revealing her husband’s secret and then pressured him into telling it…”
>
### `label_three`:"trivia"

**Definition:**
The comment's main content is information from outside the
movie itself — behind-the-scenes facts, cast and crew background, interviews,
real-life events, or other books, shows, and films.

**Example 1:**
“Saw an interview with Gisondo, he said that was the very first scene he filmed… RPat did that completely improvised.”
**Example 2:**
“I think this type of thing is what I have been missing in the MCU for a while.”

### The hardest boundary

**Which two labels:** `reaction` vs `analysis`

**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's `analysis`, even
     if the tone is heated." -->

If the comment gives a **reason tied to a specific moment in the film**
(it names or describes a scene, line, shot, or plot event AND says why it
matters), it's `analysis` — even if it starts with "I loved" or is full of
emotion. If it only says *that* a moment hit them (funny, shocking, amazing)
without saying *why*, it's `reaction`.

**Second rule (`trivia` vs the others):** If the outside fact is the main
point, it's `trivia`. If an outside fact is only a small aside inside an
argument about the film, label by the argument instead.



---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->


**Where the posts came from:**
Data come from this:

1. You Can See Everything (5k+ comments)
   (https://www.reddit.com/r/movies/comments/1x7493f/official_discussion_you_can_see_everything/)
2. Primetime (2.1k comments)
   (https://www.reddit.com/r/movies/comments/1wpk3fp/official_discussion_primetime_spoilers/)
3. Spider-Man: Brand New Day (1.2k comments)
   (https://www.reddit.com/r/movies/comments/1vbdbnx/official_discussion_spiderman_brand_new_day/)
4. The Drama (4.5k comments) 
   (https://www.reddit.com/r/movies/comments/1sb0qvz/official_discussion_the_drama_spoilers/)





**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

I read and label them one by one. For example"
- reaction: the commenter reports their own feeling or experience of the movie without explaining why it works
- analysis: a claim about a character, theme, or filmmaking choice supported by a specific scene, line, or shot from the film
- trivia: information from outside the movie — behind-the-scenes, cast background, interviews, real events, or other works

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| reaction  | 111 | 44.4% |
| analysis | 99 | %39.6 |
| trivia | 40 |  16.0%|
| **Total** | 250 | 100% |

No label is over 70%

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:*
> "Also a teacher here. I taught high school for nearly 10 years, and I've been teaching middle school for the past few years. I agree that the movie explored the sensitive topic well. Especially at the middle school level, kids' brains are on fire these days. They are bombarded with and exposed to so many things, from silly nonsense to mildly harmful brainrot to all kinds of bullying to dysfunctional home lives to the worst things imaginable an easy click away on the internet. All these things affect kids in different ways to different degrees. I really admired how the movie stuck to its premise that Emma truly didn't have a reason for why she was about to commit such a horrible act that others would "accept." It was amusing how her friends, especially her partner, were trying to find a way to rationalize it. Yet sometimes people just do terrible things with motivations that others can't understand or buy into. The whole aesthetic thing for . I also want to mention that I've already listened to "Inside Out" by Odyssey at least 6 times since seeing the movie yesterday."
> *Could have been:*
> trivia → reaction
> *I chose, because:*
I chose reaction instead on AI pre-suggestion because it ia very long comment that commentator
 tried to explain there movie situation to their reaction more than trivia ( something not relate to the movie)
 **2.**
> *The post:*
> “I think that was symbolic of the internet connection?”
> *Could have been:*
> analysis → trivia
> *I chose, because:*
I chose trivia because no movie details ( they focus on internet connection) that can be for commenting on other comments.
**3.**
> *The post:*
> "*"When we come bAaAck, the parade of men BEE-gins, and they COME... bearing geee-afts."*"
> *Could have been:*
>  reaction -> trivia
> *I chose, because:*
I chose trivia because it unclean that they focus on the movie, and they seem playing the wording
---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:**

`distilbert-base-uncased` (the notebook default)

**Settings:** <!-- epochs, learning rate, batch size, seed -->
3 epochs, learning rate 2e-5, batch size 16, max length 128 tokens, seed 42.
Trained on: <device from section 1, e.g. cpu (CPU)>

**Anything I changed from the defaults, and why:**

I left all the hyperparameters at their defaults. This unit treats them as vocabulary,
not decisions, and I wanted the first run to be a clean reference point. The only edit was
`LABELS`, to match my taxonomy: `analysis`, `reaction`, `trivia` instead of the starter's
`hot_take`.

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->

250 rows, stratified 70/15/15 with seed 42 → train 174 / val 38 / test 38.

| label    | train | val | test |
|----------|------:|----:|-----:|
| reaction |    77 |  17 |   17 |
| analysis |    69 |  15 |   15 |
| trivia   |    28 |   6 |    6 |

`trivia` has only **6 examples in the test split** (under ~8). Each one is worth about 17
points of recall, so its F1 will move a lot between seeds. That is a property of the
small sample, not necessarily of the model.

---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:* Pre-labels for the remaining 230 posts, using my label definitions
  (`analysis`, `reaction`, `trivia`).
- *What came back:* A suggested label for each post, kept in the `ai_suggestion` column.

- *What I changed:* I read all 230. I agreed with 219 and changed 11. Examples:
  - "Some really dark, twisted trauma. She's psychotic even before she knows her sister is
    dead…": AI said `reaction`, I changed it to `analysis` because it reads the
    character's behaviour, not just a feeling.
  - "I think that was symbolic of the internet connection? It was cool": AI said `analysis`,
    I changed it to `trivia`.
  The changes went in every direction (5 to analysis, 4 to trivia, 2 to reaction), so the
  AI wasn't wrong about one single label. The borders between my labels are where it struggled.


**Moment 2**

- *What I asked for:* How to approach labelling 250 posts. I wasn't sure whether to label
  everything by hand or get help.
- *What came back:* Two options: (1) label everything myself, or (2) label a first batch
  myself "cold", then let an AI pre-label the rest and check every one.

- *What I changed:* I chose option 2, but I labelled 20 posts cold first, before seeing any AI
  suggestion, so my own decision rule was set before the AI could influence it. I wrote a
  short reason for each one in the `note` column.


**Pre-labelling disclosure:**

20 of 250 rows were labelled by me cold, with no AI input. The other 230 were pre-labelled
by an AI, and I read and checked every one myself. The AI's original suggestion is kept in the
`ai_suggestion` column, and the `note` column marks each row as `cold`, `pre-labelled, checked`,
or `pre-labelled, checked — changed by me` (11 rows), so anyone can compare.



<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.395 | 0.711 | +0.316 |
| Macro F1 | 0.189 | 0.513 | +0.324 |
| F1 — `analysis` | 0.566 | 0.727 | +0.161 |
| F1 — `reaction` | 0.000 | 0.811 | +0.811 |
| F1 — `trivia` | 0.000 | 0.000 | +0.000 |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

I did not write a prediction down before running the trained model, so I can't claim one. 
What I expected going in: "that fine-tuning would beat the zero-shot baseline, but I wasn't sure by how much, and I thought trivia would be the hardest label because it's the smallest". What surprised me:  "the baseline got 0 F1 on reaction, it never predicted it at all"

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->

- The baseline didn't really classify anything. In baseline_results.json, the zero-shot model labelled all 38 test posts as analysis (analysis recall = 1.0, precision = 0.39 = 15/38). Its 39.5% accuracy is just the share of test posts that happen to be analysis. It never got a reaction or trivia right.
- Fine-tuning added nothing for trivia. In results.json the trained model also never predicts trivia: all 6 trivia posts went to analysis (4) or reaction (2). Its F1 is 0.00 for both models. Your table is missing that row. Add | F1 — trivia | 0.000 | 0.000 | +0.000 | so the gap is visible. This is also why macro F1 is only 0.51 even though accuracy is 0.71.
  - The test set is small. With 38 posts, each one is worth about 2.6 accuracy points, so read +0.316 as "clearly better," not as a precise figure.
---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Balance  |Each label 15-50% of data | 44/40/16% | same |same | Pass: a dataset fact, so it's the same for every seed |
| 2. Consistency | >= 70% agreement with staff | 93.3% (28/30) | same  | same  |Pass: doesn't depend on the seed  |
| 3. Confidence |conf >= 0.8 rigth >= 75%  | - | - | - | 	Can't measure: mean confidence is about 0.44, so almost nothing reaches 0.8. See below |
| 4. Pre-label | Every label F1 >= 0.40 (revised in unit 6) | min F1 0.00 | 0.00 |0.00  | Miss: trivia F1 is 0 on every seed |
| 5. Accuracy | >= 0.60 on all three seeds (revised in unit 6) | 0.711    | 0.632 |0.526  | Miss: seed 2024 is below 0.60 |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted | reaction |analysis  | trivia |
|---|---|---|---|
| reaction |  15| 2 |0  |
| analysis | 3 |12  |0  |
| trivia | 2 |4  | 0 |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->

4 real trivia posts were called analysis and none went the other way, so the model never learned trivia as its own label and treats factual posts as analysis.

---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Balance | Each label 15–50% of the data | MET | Split is 44 / 40 / 16%, all inside 15–50%. It's a dataset fact, so it's the same on every seed. Trivia at 16% is only just above the floor. |
| 2 | Consistency | ≥ 70% agreement with staff | MET | 28/30 = 93.3% from `agreement.py`, well above 70%. It doesn't depend on the seed. |
| 3 | Confidence | Predictions with conf ≥ 0.8 are right ≥ 75% of the time | MISSED | Mean confidence is about 0.43–0.44 on every seed, so almost no prediction reaches 0.8 and the model is never confident enough to meet the target. Accuracy of the most-confident third (0.83 / 0.92 / 0.67) also drops below 75% on seed 2024. |
| 4 | Per-label F1 | Every label F1 ≥ 0.40 on all seeds (revised in unit 6) | MISSED | Trivia F1 is 0.00 on seeds 42, 7 and 2024. The model never predicts trivia (confusion-matrix column is all 0). |
| 5 | Accuracy | ≥ 0.60 on all three seeds (revised in unit 6) | MISSED | 0.711 / 0.632 / 0.526. Seed 2024 falls below 0.60, so it doesn't hold on all three. |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->

**First, is it a labelling problem or a model problem?** My agreement with
staff was 28/30 = 93%, well above my 70% target. I can apply a written
taxonomy consistently, so my 250 labels are unlikely to be noisy enough to
explain the misses below. Both of my disagreements with staff were about
`hot_take`, which isn't one of my labels, so neither tells me anything about
the reaction / analysis / trivia boundaries. That points the misses at the
model and the data size rather than at inconsistent labelling.

**#4 Per-label F1 (missed): too few examples for trivia.** Trivia is 40 of
250 posts (16%), so only about 34 reach training and 6 reach the test split.
The model never predicts trivia on any seed: the trivia column of the
confusion matrix is 0 on all three. Where the 6 trivia posts go depends on the
seed. On seed 42, 4 went to analysis and 2 to reaction. On seed 2024, all 6
went to reaction. If the trivia/analysis boundary were the problem, the errors
would go one way consistently. Instead the model ignores the smallest label
and sends those posts to whichever large label is nearest, which is the
pattern you get from too few examples.

**#5 Accuracy (missed): the task is out of reach at this data size, made
worse by #4.** Accuracy ranges from 0.711 to 0.526 depending only on the seed.
A 0.19 swing from reshuffling the same 250 posts means the model hasn't learned
a stable boundary. On seed 2024, 8 of 15 analysis posts were called reaction,
compared with 3 on seed 42. Every trivia post is also guaranteed wrong (6 of
38 test posts = 16%), so the ceiling is about 0.84 before any other mistakes.

**#3 Confidence (missed): the model is unsure about everything.** Mean
confidence is 0.43–0.44 whether the prediction is right or wrong, which is
barely above the 0.33 baseline for three labels. Nothing reaches 0.8, so the
model can't separate its good predictions from its bad ones by confidence. It
is the same cause as #5: with about 210 training posts, the model hasn't moved
far from guessing.



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** 28 / 30 =  93%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

**1.**
> *The post:*
>Times are down about 3% since the shoe rules changed, so obviously the shoes are the whole story and the sport has a problem.

> *Staff said / I said:*
> `hot_take` / `analysis`

> *My call, and why:*
> Staff is right: `hot_take`. Rule 1 asks whether the fact carries the
> argument. Here it doesn't: "so obviously the shoes are the whole story"
> jumps to a conclusion the 3% can't support, and nothing rules out other
> causes. It is almost word for word the taxonomy's own `hot_take` example.
> I labelled it `analysis` because I saw a number, which is the exact
> mistake rule 1 exists to prevent.
>
> *Which pile:*
> *Which pile:*
(a) the rule covered it and you applied it loosely — a consistency problem
**2.**
> *The post:*
> Nobody actually enjoys the long run. They enjoy having done it, which is a completely different thing, and the sport would be more honest if it said so.
> *Staff said / I said:*
> `hot_take` / `reaction` 
> *My call, and why:*
> Staff is right: `hot_take`. Rule 2 asks whether the post is about the
> writer or about the world. "Nobody actually enjoys the long run" is a
> general claim about every runner, not a report of something that just
> happened to the writer. There is no event, no "I", and no recent moment.
> I went with `reaction` because of the feeling word "enjoy", but rule 2
> says strength of feeling doesn't decide it. The claim does.
>
> *Which pile:*
(a) the rule covered it and you applied it loosely — a consistency problem

**What the pattern in my disagreements tells me:**

Both disagreements are pile (a), and both come from the same habit: I
labelled from a surface cue instead of applying the rule. A number made me
pick `analysis`, and a feeling word made me pick `reaction`, while the rules
say to check whether the number does any work and whether the claim is about
the writer. Both posts were ones staff marked as hard, and I agreed on the
other 28, so it's not widespread. The same habit could still be in my own 250
labels, though: a trivia post with a number in it may have been labelled
`analysis` for the same reason, which would blur the trivia/analysis boundary
the model already fails on (seed 42 sent 4 of 6 trivia posts to analysis).

---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**

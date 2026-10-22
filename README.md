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
My community is r/Swimming, a public subreddit where people ask for advice on technique, training, and gear. My classifier sorts each post into one of two labels: `question`, where the poster is mainly asking for advice or information, or `experience_share`, where the poster reports something that happened to them without asking for help. The line between them is whether the post contains an explicit ask. Posts that share a lot of personal experience but end with a request still count as `question`.

---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `question`

**Definition:** The post's goal is to receive advice, information or tips, even if it includes the poster's own background.

**Example 1:**
> Nose pressure doesn't allow me to swim. hello,
>
> I feel ridiculous for posting this because everyone seems to be able to do it fine but whenever I swim more than a few strokes, the pressure in my nose gets too high and when I inhale through my mouth out of the water the water inside my nose comes into my mouth and I feel like I’m drowning. it gets worse as I keep swimming longer. I can’t breathe/hum all the pressure out my nose in time before I have to come to breathe up again. it makes freestyle and breaststrke very hard but butterfly literally impossible.
>
> ive tried closing some muscle in the back of my throat right before breathing in. but it takes me a solid second to do so and I mess it up sometimes and water comes flooding in. It does keep water out though if I do it properly
>
> this also causes me to not be able to get enough air in before everything starts to turn black (I think?)
>
> thanks




**Example 2:**
> Total beginner - some help please. I’ve started adult beginner swimming lessons , never swam before and was scared of even getting face in the water.
>
> I’m on lesson 4, I’ve gotten decent at front float (with or without aid) , back float with noodle, treading with noodle and surprisingly no issue with submerging face in water. I thought I was doing good until…
>
> My last 2 lessons which have involved using a single arm for the pull with a board and side breathing while on front with board. Breathing I thought I nearly got it but when I come for breath my propulsion forward seems to stop and other times I panic breath and swallow water
>
> I’m struggling with these things, mainly the breathing which is fine when I’m doing practice drills (face in, exhale , face out inhale) but as soon as I start front swimming I lose all my ability to breathe or coordinate. Any tips or practice drills people can recommend that I can do outside my lessons? Or even any advice at all

### `experience_share`

**Definition:** The post reports something the poster did or experienced in the water, shared with the community and not explicitly asking for help.

**Example 1:**
> Finally clicked! I used to tire myself so much swimming front crawl (which surprised me because I can swim breaststroke pretty fast and for long distances) and only today realised that I've been over-kicking. Timed it to a 2-kick/stroke rhythm and swam so much more easily. Didn't realise I'd been tiring myself out and wasting energy. Keeping to the rhythm and being disciplined with that is helping a lot. Thank you to everyone who has talked about kicking here -- ended up passively absorbing a very helpful tip!

**Example 2:**
> Flip turns as a beginner
> Today's lesson I wanted to have a go at doing flip turns. After about 5/6 goes pushing off onto my back from Front Crawl. I couldn't mentally work out how to turn onto my stomach. Kept swerving into the lane divider. And getting tangled up and dizzy.
>
> Doesn't help when only in 1.2 mtr water!

### The hardest boundary

**Which two labels:** 'question' and 'experience_share'

**The decision rule I used every time:**
<!-- e.g. "If the post names a specific checkable fact, it's `analysis`, even
     if the tone is heated." -->
If the post explicitly asks for advice, tips, or help (a question or a direct request), it's `question`, even when most of the text is personal experience. If there's no explicit ask, it's `experience_share`, even if the poster seems to be hoping for replies.

**Example of the boundary:** The 'Flip turns as a beginner' post. It describes a struggle and never asks for help, so under my rule it's `experience_share`.


---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:** Public r/Swimming posts. Reddit blocked scripted access from my network, so I saved listing JSON from my browser and converted it to labels.csv with a Python script. Posts with no body text, removed or deleted posts, and mod threads were dropped, and duplicates were removed. This is not a random sample: most r/Swimming posts are questions, so I searched for progress and milestone posts to find enough experience_share examples, then sampled to balance the classes. A live feed would be mostly questions.

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->
I labelled 20 posts cold, with no AI label shown. AI pre-labelled the other 150 using my written rule, and I reviewed them afterwards: 140 marked checked, 10 corrected by me, and 0 not individually verified.

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| `question` | 96 | 56.5% |
| `experience_share` | 74 | 43.5% |
| **Total** | 170 | 100% |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:* "Summer McIntosh 200 Fly WR", a news post about a world record with no ask.
>
> *Could have been:* experience_share (no ask), or neither, since the poster did not do or experience anything in the water.
>
> *I chose, because:* experience_share, because my rule says no explicit ask means experience_share and it was the closest fit.

**2.**
> *The post:* "Started swimming classes while having aquaphobia". Mostly a progress story, but it near the end says "Any tips for an absolute beginner (with a phobia), are welcome!"
>
> *Could have been:* experience_share (the story is most of the text) or question (it closes with a request for tips).
>
> *I chose, because:* question, because the closing line is an explicit request for tips, and my rule says an explicit ask makes it a question even when most of the post is personal experience.

**3.**
> *The post:* "Told an old lady to shut up today". A story about a confrontation at the pool.
>
> *Could have been:* experience_share (it recounts something that happened) or question (it ends by asking whether they should have shared the lane).
>
> *I chose, because:* question, because it ends with an explicit question asking for a judgment, and my rule treats an explicit ask as the deciding factor.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:** distilbert-base-uncased

**Settings:** <!-- epochs, learning rate, batch size, seed --> 3 epochs, learning rate 2e-5, batch size 16, seed 42, max length 128. Hardware: Apple Silicon GPU (device mps), torch 2.14.1.

**Anything I changed from the defaults, and why:** Nothing. I used the notebook's default training settings. The only edits to the notebook were setting LABELS to ["question", "experience_share"] and NAME to my name.

**Split sizes:** <!-- train / val / test, and per-label counts in the test
split. If a label had fewer than about 8 in test, say so — it explains a lot
of next unit's variance. -->
train 118 / val 26 / test 26 (70/15/15). Per-label test counts: question 15, experience_share 11. Neither label is under 8 in test, but 26 test posts is small, so one post moves accuracy by about 4 points. The dataset is 170 rows, under the 200 the brief asks for.

Result for seed 42: accuracy 0.577, macro F1 0.366. The model predicted question for all 26 test posts, so experience_share F1 was 0.000. 0.577 is just the share of question posts in the test split, so this run did not learn the boundary. I'll diagnose it in unit 6 across three seeds.



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Pre-labelling disclosure:**

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy |  |  |  |
| Macro F1 |  |  |  |
| F1 — `label_one` |  |  |  |
| F1 — `label_two` |  |  |  |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

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
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**2.**
> *The post:*
>
> *Staff said / I said:*
>
> *My call, and why:*
>
> *Which pile:*

**What the pattern in my disagreements tells me:**



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

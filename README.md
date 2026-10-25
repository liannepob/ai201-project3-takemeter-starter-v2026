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

- *What I asked for:* I asked Claude Code to run section 1, section 6 and section 7 of the notebook for the before and after three-seed runs, without re-running the section 5 lines that overwrite results.json and test_split.csv, and to fill in both Run Log tables from criteria.md and the JSON files.
- *What came back:* The per-seed numbers, the confusion matrix, and both Run Log tables filled with my criteria and the per-seed values. It also pointed out that the before run's zero spread was the same all-question failure three times, not stability, and that criteria 4 and 5 had no number it could fill in.
- *What I changed:* I checked the numbers against the notebook output and the JSON files.

**Moment 2**

- *What I asked for:* I asked Claude Code to draft the verdicts and the diagnosis paragraphs, and later this end-of-unit write-up, in first person and using only facts I supplied plus the JSON numbers.
- *What came back:* Draft verdicts, the Verdicts and Diagnoses table, and short diagnosis paragraphs. It also flagged that my agreement report was missing, so the diagnoses couldn't separate a labelling problem from a model problem.
- *What I changed:* I supplied the facts the drafts had to use and checked them against the README numbers, and I kept the wording as drafted rather than rewriting it.

**Pre-labelling disclosure:** I labelled 20 posts cold, with no AI label shown. AI pre-labelled the other 150 using my written rule, and I reviewed them afterwards: 140 checked, 10 corrected by me, and 0 not individually verified.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 0.500 | 0.577 | +0.077 |
| Macro F1 | 0.461 | 0.366 | -0.095 |
| F1 — `experience_share` | 0.606 | 0.000 | -0.606 |
| F1 — `question` | 0.316 | 0.732 | +0.416 |

**What I predicted before I looked:**

<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

My seed 42 model called every test post `question`, so I expect the baseline to beat it on `experience_share`. I expect the baseline to still struggle on posts that tell a story and end with a small ask, since that's my hardest boundary.

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->
The trained model beat the baseline on accuracy (0.577 against 0.500) only because it called every post question, and 15 of the 26 test posts are question. The baseline was the better classifier on experience_share, with an F1 of 0.606 against my model's 0.000, and it also had the higher macro F1 (0.461 against 0.366), so at that point fine-tuning added nothing. The baseline leaned the other way, catching 10 of 11 experience_share posts but only 3 of 15 question posts. Both models were scored on the same 26 posts, but that is the seed 42 test split only, so I have no baseline numbers for seeds 7 and 2024.



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Accuracy is at least 0.75 on the held-out test set. | ≥ 0.75 | 0.577 | 0.577 | 0.577 | MISSED |
| 2. Each label has an F1 of at least 0.65 on the held-out test set. | ≥ 0.65 each | question 0.732 · experience_share 0.000 | question 0.732 · experience_share 0.000 | question 0.732 · experience_share 0.000 | MISSED |
| 3. No label is more than 60% of labels.csv. | ≤ 60% | 56.5% (question 96/170) | 56.5% (question 96/170) | 56.5% (question 96/170) | MET |
| 4. On the 20 posts I labeled cold, I agree with my own re-labels at least 85% of the time. | ≥ 85% | not measured | not measured | not measured | NOT MEASURED, I haven't re-labelled them yet |
| 5. Predictions with confidence above 0.80 are correct at least 80% of the time. | ≥ 80% | not recorded (most-confident third: 0.750) | not recorded (most-confident third: 0.750) | not recorded (most-confident third: 0.875) | NOT MEASURED, per-post confidence wasn't saved |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

Seed 42 (section 7 prints the first seed; seeds 7 and 2024 produced the identical matrix):

| true \ predicted | question | experience_share |
|---|---|---|
| **question** | 15 | 0 |
| **experience_share** | 11 | 0 |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->
11 real experience_share posts were called question and 0 went the other way, identically on all three seeds, so the model never learned the question/experience_share boundary and defaulted to question every time.



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 | Accuracy is at least 0.75 on the held-out test set. | ≥ 0.75 | MISSED (before and after) | Before: 0.577 on seeds 42, 7 and 2024. After: 0.692 (seed 42), 0.500 (seed 7), 0.654 (seed 2024). Every seed in both runs is below 0.75, and seed 7 after is the lowest. |
| 2 | Each label has an F1 of at least 0.65 on the held-out test set. | ≥ 0.65 each | MISSED (before and after) | Before: question 0.732 on every seed, but experience_share 0.000 on every seed, so all three seeds break it. After: experience_share 0.600 / 0.133 / 0.526 (seeds 42 / 7 / 2024), below 0.65 on all three. question 0.750 / 0.649 / 0.727, so seed 7 also misses on question. |
| 3 | No label is more than 60% of labels.csv. | ≤ 60% | MET | question is 96 of 170 rows (56.5%) and experience_share is 74 (43.5%). This is a property of labels.csv, so it is the same on every seed and in both runs. |
| 4 | On the 20 posts I labeled cold, I agree with my own re-labels at least 85% of the time. | ≥ 85% | NOT MEASURED, I haven't re-labelled them yet | No seed produces this number. It needs a second labelling pass over my 20 cold posts, which I haven't done. |
| 5 | Predictions with confidence above 0.80 are correct at least 80% of the time. | ≥ 80% | NOT MEASURED, per-post confidence wasn't saved (counted as not met) | The notebook saves accuracy for the most and least confident thirds, not each post's confidence, so I can't check the 0.80 cutoff. For reference, the most-confident third scored 0.750 / 0.750 / 0.875 before and 0.875 / 0.750 / 1.000 after (seeds 42 / 7 / 2024). |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->

**Criteria 1 and 2, before (3 epochs).** The model called every test post question on all three seeds. The matrix has 11 experience_share posts called question and 0 the other way, and accuracy is 0.577, which is exactly the question share of the test split (15/26). The zero spread across seeds is the same failure three times, not stability. Raising epochs to 10 changed this, which tells me too little training was part of the cause.

**Criterion 1, after (10 epochs).** Accuracy is 0.692, 0.500 and 0.654, so every seed is still under 0.75, and the spread is 19.2 points. With only 26 test posts, one post moves accuracy by about 4 points, so a swing this big means the measure itself is unstable. I think the main cause is too little data, since the model only trains on 118 posts.

**Criterion 2, after (10 epochs).** The model now predicts both labels, but experience_share F1 is 0.600, 0.133 and 0.526, below 0.65 on every seed, and seed 7 caught only 1 of its 11 experience_share posts. Only 11 experience_share posts land in each test split, so a few posts swing this score a lot. The boundary is also fuzzy in my own data: hard cases 2 and 3 are personal stories that I labelled question because of a closing ask, which may teach the model that story-like posts are question.

**What I can't tell yet.** My agreement report against the staff set is not available yet, so I can't separate a labelling problem from a model problem. Until I have it, too few examples and a fuzzy boundary are both possible causes for the experience_share misses, and I can't say which matters more.

**Criteria 4 and 5.** Neither produced a number. Criterion 4 needs a re-labelling pass I haven't done. Criterion 5 can't be checked as written because the notebook doesn't save each post's confidence, so I count it as not met.



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** ___ / 30 = ___%

Not completed. I labelled all 30 staff posts under the staff taxonomy (my_staff_labels.csv), but I didn't have data/staff_labels.csv from my TF before the deadline, so I couldn't run agreement.py or adjudicate any disagreements.

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

**What I changed:** Raised epochs from 3 to 10, one change only.

**Which diagnosis pointed at it:** The before matrix showed every post called question on every seed, which looked like an under-trained model, so I raised epochs from 3 to 10. My agreement report against the staff set wasn't available, so I couldn't separate a labelling problem from a model problem, and this was a best guess. Training changes are usually not what a diagnosis points at, so I treat this as a test of the under-training idea rather than a fix the evidence demanded.

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1. Accuracy is at least 0.75 on the held-out test set. | ≥ 0.75 | 0.692 | 0.500 | 0.654 | MISSED |
| 2. Each label has an F1 of at least 0.65 on the held-out test set. | ≥ 0.65 each | question 0.750 · experience_share 0.600 | question 0.649 · experience_share 0.133 | question 0.727 · experience_share 0.526 | MISSED |
| 3. No label is more than 60% of labels.csv. | ≤ 60% | 56.5% (question 96/170) | 56.5% (question 96/170) | 56.5% (question 96/170) | MET |
| 4. On the 20 posts I labeled cold, I agree with my own re-labels at least 85% of the time. | ≥ 85% | not measured | not measured | not measured | NOT MEASURED, I haven't re-labelled them yet |
| 5. Predictions with confidence above 0.80 are correct at least 80% of the time. | ≥ 80% | not recorded (most-confident third: 0.875) | not recorded (most-confident third: 0.750) | not recorded (most-confident third: 1.000) | NOT MEASURED, per-post confidence wasn't saved |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->

Partly. Averaged over the three seeds, accuracy went from 0.577 to 0.615, macro F1 from 0.366 to 0.564, and experience_share F1 from 0.000 to 0.420, and the model now predicts both labels on every seed. Seeds 42 and 2024 beat the all-question accuracy of 0.577 (0.692 and 0.654), but seed 7 caught only 1 of 11 experience_share posts and scored 0.500. The accuracy spread went from 0.0 to 19.2 points, and with 26 test posts one post is about 4 points, so one change can't separate a real gain from a lucky split.



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->

**Criterion 1 (accuracy at least 0.75).** I would label more posts, especially experience_share, and use a larger test split so one post moves accuracy by less than 4 points. I stopped because I ran out of time before the deadline.

**Criterion 2 (every label F1 at least 0.65).** experience_share is still the weak label (0.600, 0.133 and 0.526 after the fix), so I would add more experience_share posts and check my boundary against the staff agreement report before relabelling anything. I stopped because the unit allows one improvement and I used it on epochs.

**Criterion 4 (self-agreement at least 85%).** I would re-label the 20 cold posts blind with blind_relabel.py and compare against my original labels. I wrote the script but ran out of time to do the re-label.

**Criterion 5 (confidence above 0.80 correct at least 80% of the time).** I would change the notebook to save each post's confidence so the 0.80 cutoff can actually be checked. I stopped because changing the notebook would have been a second change in this unit.



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->
I meant question and experience_share to turn on whether the post makes an explicit ask, but the matrix shows the model mostly learned to predict question and misses experience_share posts (all 11 before the fix, and 5, 10 and 6 of 11 after it). My guess is that posts like my hard cases 2 and 3, which tell a story but end with a small ask and so are labelled question, taught the model that story-like posts are question, which makes it miss real experience_share stories that have no ask.



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

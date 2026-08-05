# Facilitation Guide — AI Basics

Every activity carries a learner-visible **"Why this matters"** line, and
every teaching section has (1) an **interactive tool or play moment**,
(2) a **labeled, timed activity** — *As a group* (classroom edition) or
*On your own* (both editions) — and (3) a **validation point**.

The full runbook lives in [`facilitator/notes.json`](facilitator/notes.json)
on the **ATD facilitator-guide framework**: per section a verbatim **Say**
script, **Do** choreography, an **Ask** with anticipated responses, a
**Debrief** line, and a scripted **Transition**, plus front matter
(materials, prep checklists, contingencies, tough questions, and
copy-paste templates: pre-work invite, 7-day pulse, AI 201 graduation note).

**Audience:** absolute beginners — people who have never opened an AI
tool, or tried once and gave up. The register is the method: no jargon,
no assumptions, no question too basic. **Pre-work:** bring one
words-shaped chore from a normal week.

The **facilitator edition is live at `/facilitator/`**, and the
**self-paced web edition at `/web/`** — regenerate both after any change
to `index.html` (facilitator also after `notes.json`):

```bash
python3 tools/build-facilitator.py
python3 tools/build-web.py
```

## Run of show — two paths

| Slide | Full (60 min) | Core (30 min) |
|---|---|---|
| Welcome / QR | 3 | 2 |
| What you'll get | 2 | 1 |
| The plan | 1 | — |
| 01 What is AI? | 8 | 4 |
| Manifesto | 1 | — |
| 02 Why & how | 8 | 4 |
| 03 When & when not | 9 | 5 |
| 04 What it can do | 8 | 4 |
| 05 Your first try | 10 | 6 |
| Recap quiz | 4 | 2 |
| My First Try (capstone) | 4 | 1 |
| Closing / commitment | 2 | 1 |
| **Total** | **60** | **30** |

**Core-path rules (the lunch-and-learn):** every trainer stays as a fast
room vote, the live demo shrinks to one exchange, group rounds become one
voice each — but the prompt builder and the commitment card run at full
length. They ARE the outcome. Per-section cuts live in each `coreNote`.

**Timing discipline:** Idea 05 (the builder and in-room first try) is the
conversion moment — protect its 10 minutes by trimming debriefs anywhere
else. Never cut the traffic-light trainer or the prompt builder.

## Validation model

- **In the moment:** trainer scores (01, 02, 03, 04), the inline check
  (03), the live demo's before/after (02), and the assembled, copied
  prompt on every screen (05).
- **End of session:** the 5-question recap maps to the five ideas
  (Level 2); the closing fist-to-five is the Level 1 check; the My First
  Try card and the chore-and-day commitment round are the transfer
  artifacts.
- **After:** the 7-day pulse (did the first try run, did the follow-up
  trick work) is the Level 3 evidence — **the count of completed first
  tries is the program's headline metric**, because this course exists to
  convert non-users into users. Confident finishers get routed to AI 201.
- **Consistency guard:** the traffic light must always match AI 201's
  green/yellow/red rules; the two courses cite each other.

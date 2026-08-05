# AI Basics — Vanderbilt Learning Series

Single-page interactive classroom experience (Learning on Demand), pared
to a true absolute-beginner course. Live at
https://me5231979.github.io/AI_Classroom/ (GitHub Pages, served from the
`gh-pages` branch — publish with `git branch -f gh-pages main && git push -f origin gh-pages`).

Sequel: AI-Advanced (AI 201). Catalog: me5231979/Course_Library.
Same engine and standing principles as the sister courses.

## Three editions, two generated

1. **Classroom** (`index.html`) — QR welcome, group activities, projected.
2. **Web / self-paced** (`web/index.html`) — GENERATED, never hand-edited:
   `python3 tools/build-web.py`. Same course minus the welcome/QR slide
   and every element tagged `data-classroom` (the "As a group" blocks and
   room-facing lines). Keep solo variants untagged so they survive.
3. **Facilitator** (`facilitator/index.html`) — GENERATED, never
   hand-edited: `python3 tools/build-facilitator.py` from
   `facilitator/notes.json`. QR encodes the LEARNER url.

REGENERATE BOTH after any change to index.html (and the facilitator after
notes.json changes), then publish.

## Standing design principles (do not regress these)

1. **Absolute-beginner register.** Audience has never opened an AI tool.
   No jargon anywhere: say "it learned from examples," never "model,"
   "LLM," or "training data." One idea per section, five sections total.
2. **Interactions throughout, kept dead simple.** Four trainers, one
   prompt builder, one commitment card, scored recap. Every section still
   has a play moment — simple is not passive.
3. **Every section facilitatable, learning validatable.** ATD runbook in
   `facilitator/notes.json` (timing must sum: Full 60 / Core 30).
   Kirkpatrick: L1 fist-to-five, L2 recap, L3 first-try card + 7-day
   pulse (first-try count is the program metric).
4. **The traffic light must stay consistent with AI 201:** green
   (public/generic), yellow (internal → approved VU tools only), red
   (private info about people → never). Never contradict the sequel.
5. **Classroom/web split via `data-classroom`.** Anything room-only gets
   the attribute; build-web.py strips it and asserts none survive.
6. **Brand: Vanderbilt FLH system.** Black #1C1C1C / white / flat gold
   #CFAE70; Libre Caslon Display headlines (one italic word), Inter body,
   Antonio eyebrows; motion ≤400ms; real VU lockups (authorized use only).
7. **No frameworks.** One CSS file, one JS file, vendored QR lib,
   self-hosted fonts; hero montage streams from Higgsfield CDN with the
   particle canvas fallback.

## Layout (12 slides, 5 ideas)

Welcome/QR (classroom only) → Hero (5 objectives + skills row + montage)
→ Agenda → 01 What is AI? (Is That AI? trainer) → manifesto ("You don't
need to know how the engine works to drive the car.") → 02 Why & how
(3-step cards + Pick the Next Move trainer) → 03 When & when not
(traffic-light cards + color trainer + inline check) → 04 What it can do
(five superpowers + matcher) → 05 Your first try (prompt builder →
copyable prompt) → Recap (5 Qs) → Capstone My First Try card → Closing.

## Editing map

- Copy: `index.html` · Recap: `QUESTIONS` in `assets/js/main.js`
- Trainers: `makeTrainer` configs (isAI, followUp, lightJudge, superPower)
- Prompt builder: `firstPrompt` block (TASKS/FORMATS) in main.js
- Capstone maps: `POWER` / `WHEN` in main.js
- Runbook: `facilitator/notes.json` (Full 60 / Core 30)
- Web edition: `tools/build-web.py` · Facilitator: `tools/build-facilitator.py`
- The old deep 17-slide course (rings, neural net, token predictor,
  temperature, ethics, wellbeing) lives in git history before the
  "pare down" commit; AI 201 now carries the depth.

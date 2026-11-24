#!/usr/bin/env python3
"""Generate the self-paced web edition at web/index.html.

Same course as the classroom edition (index.html) minus the classroom
prompts: the QR welcome slide, all "As a group" activities, and any
element tagged data-classroom. Run after editing index.html:

    python3 tools/build-web.py
"""
import re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = open(os.path.join(ROOT, 'index.html')).read()

# ---- 1. drop the welcome/QR slide (classroom only) ----
s = re.sub(r'  <!-- ============ 0 · WELCOME / QR \(classroom only\) ============ -->.*?</section>\n\n',
           '', s, flags=re.S)

# ---- 2. drop every element tagged data-classroom ----
s = re.sub(r'[ \t]*<div class="deeper__ask" data-classroom>.*?</div>\n', '', s, flags=re.S)
s = re.sub(r'[ \t]*<p class="why" data-reveal data-classroom[^>]*>.*?</p>\n', '', s, flags=re.S)
s = s.replace('<li><a href="web/" data-classroom>Self-paced web version</a></li>',
              '<li><a href="../">Classroom edition (for facilitators)</a></li>')

# ---- 3. head: title, canonical, descriptions ----
s = s.replace('<title>AI Basics | Vanderbilt</title>',
              '<title>AI Basics: Self-Paced | Vanderbilt</title>')
s = s.replace('href="https://futureslearninghub.github.io/AI_Classroom/"',
              'href="https://futureslearninghub.github.io/AI_Classroom/web/"')
s = s.replace('content="https://futureslearninghub.github.io/AI_Classroom/"',
              'content="https://futureslearninghub.github.io/AI_Classroom/web/"')

# ---- 4. asset + link paths (one directory deeper) ----
s = s.replace('href="assets/', 'href="../assets/')
s = s.replace('src="assets/', 'src="../assets/')
s = s.replace('href="cheatsheet.html"', 'href="../cheatsheet.html"')
s = s.replace('href="worksheet.html"', 'href="../worksheet.html"')

# ---- 5. cosmetic: initial slide counter ----
s = s.replace('<span class="deckbar__count" id="deckCount">1 / 12</span>',
              '<span class="deckbar__count" id="deckCount">1 / 11</span>')

assert 'data-classroom' not in s, 'a classroom-tagged element survived'
out = os.path.join(ROOT, 'web', 'index.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w').write(s)
print(f'wrote {out}')

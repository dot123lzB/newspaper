# The Morning Dispatch — daily edition spec (v2, "Plan B": light 6-7 page issue)

Personal English-language daily newspaper for a Japanese reader studying English. ONE A4 PDF, delivered via SendUserFile BEFORE 07:00 JST.

## Timing (hard)
- Run starts ~06:30 JST. US cash close is 06:00 JST (Nov-Mar; 05:00 JST in summer time, check), so US/Europe/FX numbers are final.
- 06:30-06:41 research (parallel tool calls in batches; ~15-20 searches/fetches total; deep dive <=5). 06:41-06:51 write HTML. 06:51-06:56 fit check, render, look at pages, deliver.
- At 06:52 deliver whatever is complete (drop optional blocks first). A late perfect issue is worse than an on-time slightly lighter one. Never use the extended-research tool. WebSearch mode "standard".
- Nobody can answer questions: decide, put caveats in the About box and the final message.

## Reader / print constraints
White background, black text only (no grey/light text), rules >=0.75pt, body >=10pt, dark navy highlights, dark green/red up/down. English only.

## Date and issue number
`TZ=Asia/Tokyo date`. Dateline "Friday, November 6, 2026". "Vol. I · No. N": N counts weekdays inclusively; 2026-11-05 = No. 2, 2026-11-06 = No. 3, 2026-11-09 = No. 4, ... (weekday editions only; skip weekends). Edition label "Standard Edition · Tokyo".

## Pages (target 6, max 7)
1. FRONT: masthead, dateline, market block, Today & Ahead, Top Story (2 columns), 3x2 contents grid (section, pages, key headline), "The Day's Column" (~150 words, Tensei-Jingo style, thoughtful, NON-partisan), legend line.
2. POLITICS & WORLD + JAPAN (Japan's most important story of the day must appear). Facts first, then "How the media framed it" box (outlet-attributed, only from what you read).
3. MARKETS & ECONOMY: market digest (what moved markets), "Stocks of the Day" (interesting individual movers with WHY + small table), GBP/JPY note (reader holds GBP/JPY), central-bank calendar.
4. SCIENCE & TECHNOLOGY (>=1 story) + SOCIETY, CULTURE, SPORTS (>=1 story each; freshest verifiable item; never present old results as new).
5. DEEP DIVE (1 page; 2 pages only if time allows): the single most important/interesting story or the market. Headline + deck + stars; 4-cell key-number strip; USE BULLET POINTS (<ul><li>) for facts, positions, what to watch; competing arguments table attributed to who said them; "What this means"; "Editor's assessment: what the evidence supports and what it does not" (labelled analysis, hedged, no predictions, no investment advice).
6. TODAY'S WORDS (every highlighted word, ~18-24) + "About this edition" box (sources, caveats, unconfirmed items, data fallbacks).
Every category (politics/world, Japan, markets, science/tech, society, culture, sports) appears every day.

## Market block (page 1)
2x4 fixed order: NASDAQ Composite; S&P 500; ACWI ETF (iShares MSCI ACWI, ticker ACWI); NIKKEI 225; USD/JPY; GBP/JPY; WTI crude; Gold (spot). Value, arrow+%change. Extras strip: Dow, TOPIX, Brent, dollar index (+ anything notable).
ACWI RULE (mandatory): never blank/"n/a". Compute daily % from the last two closes. Try WebFetch https://stockanalysis.com/stocks/acwi/ (history page may lag), search "iShares MSCI ACWI ETF ACWI close"; fall back to URTH or an MSCI ACWI index report and LABEL the instrument and date. Only if all fail: last known price with date, and say why in the About box.
Verify each number against >=1 source; if sources disagree use the more reliable and mark "≈". Never invent a figure. State the as-of basis in the legend.

## Today & Ahead
Two lines (TODAY, AHEAD). BOLD: central-bank decisions, elections/vote counts, major data (US jobs, CPI). JST times. Verify dates by search.

## Writing rules
- Each article: headline (no numbering), optional deck, CEFR meta line (★☆☆☆ A1-B1, ★★☆☆ B2, ★★★☆ C1, ★★★★ C2; e.g. "★★★☆ C1"), body, "Sources:" with real <a href> links. Own words; short attributed quotes only.
- >=1 highlighted word per article: <span class="w">word</span>; list all on the Words page (CEFR, Japanese meaning, example from the paper). Mix difficulty; some briefs B1/B2.
- Neutrality: facts first, then each outlet's/side's framing, attributed to who actually said it. No own opinion on contested politics outside the labelled Editor's assessment and the column. Election results are "projections" unless certified; say who called them. Say when you relied on a secondary report.
- No lyrics/long quotes, no images of real people, no investment advice.


## Editorial rules from the reader (2026-11-06) — apply every day
1. Multi-outlet synthesis: for each topic, check outlets across blocs (wires; US/UK/Canada papers; non-Western: Al Jazeera, SCMP, Asia Times, Times of India/The Hindu/Indian Express; business: Bloomberg/FT/Nikkei/Forbes/Foreign Affairs; Japanese papers: Yomiuri, Sankei, Asahi, Mainichi, Nikkei). Compare their stance and bias, then integrate. Time is short (25 min): for each MAJOR story read >=2-3 outlets from different blocs; rotate the rest. Say which outlets were actually read; never claim a view from an outlet you did not read (headlines/snippets count only as "headline").
2. Rewrite in your own words into ONE polished article per topic (no patchwork).
3. Difficulty gradient inside articles: open plain and accessible (B1-B2), then move to professional detail and terminology (C1-C2). Show the article's CEFR as the top level reached.
4. Quotes: personal-use study paper, so short direct quotes, quoted headlines and data are fine, always attributed. Still do not reproduce articles wholesale.
5. Classic layout (in assets/style.css): NO boxed articles (use whitespace or thin vertical rules), 2-3 column body, sans-serif headlines, serif body, DROP CAP on lead articles (add class `dc` to `.body`; start the lead paragraph with a normal word, not an abbreviation like "U.S.", and omit the `.loc` dateline there).
6. Market cells: value, change, and Day's Range (high-low) with a range bar (`tools/spark.py rangebar`) plus a sparkline (`spark`) when verified data exist. NEVER invent: if no fresh source for range/series, omit them and say so in About. Known limit: Yahoo/Stooq APIs are blocked and history pages (Yahoo, investing.com, stockanalysis history) are days to weeks stale; stockanalysis.com QUOTE pages (ETFs, e.g. ACWI) are fresh and show Day's Range and the 4 p.m. close.
7. Numbers: re-fetch quote pages near build time; if two snapshots of one instrument disagree, use the later dated one and mark "≈". Check the Day's Range/close timestamp.

## Sources
Start from SOURCES.md (tested site list, known-bad sites, search tips). Only go beyond it when a needed category is missing.

## Build procedure
1. Repo is at /home/claude/newspaper (clone https://github.com/dot123lzB/newspaper if absent; add via add_repo if needed). Fonts and CSS are in `assets/` (no npm needed).
2. Copy `examples/issue_No2_2026-11-05.html` to `work/issue.html` as the skeleton (it links ../assets/style.css) and REPLACE the content, keeping the same components and class names; delete pages you do not need and fix "Page X of N" and contents-grid page numbers. Reuse the structure of the example pages (p1 front, p2-3 politics, p4-5 markets, p5-6 sci/society, p7-8 deep dive, p9 words).
3. Fit: `python3 tools/fit.py work/issue.html` — every page must be <= 277mm and ideally >= 85% full. Trim text or move blocks; do not go below 10pt body.
4. Render: `python3 tools/render.py work/issue.html out/MorningDispatch_YYYY-MM-DD.pdf`; `pdftoppm -r 60 -png` and LOOK at every page (nothing cut, no orphan headline, footers/TOC right, total pages == N).
5. Deliver: SendUserFile (status "proactive", caption = date + lead), then SendUserMessage in Japanese (<=8 lines): lead, deep-dive topic, page count, honest caveats. If incomplete, still deliver and say exactly what is missing.
6. Optionally save the finished issue HTML+PDF under `examples/` only if asked; do not commit daily files unless instructed.

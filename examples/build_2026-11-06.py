import re, pathlib, sys
sys.path.insert(0,'/home/claude/newspaper/tools')
from spark import rangebar, spark
DATE="Friday, November 6, 2026"; SHORT="Fri, Nov 6, 2026"; N=6
def run(sec): return f'<div class="run"><span class="t">The Morning Dispatch</span><span>{SHORT}</span><span>{sec}</span></div>'
def foot(sec,p): return f'<div class="pfoot"><span>{sec}</span><span>Page {p} of {N}</span></div>'
def page(i,body): return f'<div class="page" id="p{i}"><div class="content">\n{body}\n</div></div>\n'
def a(u,t): return f'<a href="{u}">{t}</a>'
def src(*links): return '<div class="src"><b>Sources:</b> '+' · '.join(a(u,t) for u,t in links)+'</div>'
HR='<div class="hr2"></div>'

# ---------------- P1 ----------------
p1=f'''
  <div class="mast"><h1>The Morning Dispatch</h1></div>
  <div class="dateline"><span>Vol. I · No. 3</span><span>{DATE}</span><span>Standard Edition · Tokyo</span></div>
  <div class="mkt">
    <div class="c"><div class="l">NASDAQ COMP.</div><div class="v">24,315.00</div><div class="d dn">▼ −5.52%</div></div>
    <div class="c"><div class="l">S&amp;P 500</div><div class="v">7,353.73</div><div class="d dn">▼ −4.36%</div></div>
    <div class="c"><div class="l">ACWI ETF</div><div class="v">$152.43</div><div class="d dn">▼ −3.82%</div>{rangebar(150.88,158.02,152.43)}</div>
    <div class="c"><div class="l">NIKKEI 225</div><div class="v">≈61,078</div><div class="d dn">▼ −1.79%</div><div class="n">Thu close, pre-rout</div></div>
    <div class="c"><div class="l">USD/JPY</div><div class="v">≈158.40</div><div class="d up">yen ▲ +0.03%</div></div>
    <div class="c"><div class="l">GBP/JPY</div><div class="v">≈212.95</div><div class="d dn">▼ ≈−0.23%</div></div>
    <div class="c"><div class="l">WTI CRUDE</div><div class="v">$90.96</div><div class="d up">▲ +3.22%</div></div>
    <div class="c"><div class="l">GOLD (FUTURES)</div><div class="v">≈$4,100</div><div class="d up">▲ +0.67%</div></div>
  </div>
  <div class="mkt2" style="margin-top:-3.2mm;">
    <span><b>DOW</b>51,523.06 <span class="dn">▼ 3.44%</span></span>
    <span><b>VIX</b>28.18 <span class="up">▲ 69.7%</span></span>
    <span><b>BRENT</b>$98.29 <span class="up">▲ 3.9%</span></span>
    <span><b>US 10-YR</b>4.84%</span>
  </div>
  <div class="sched">
    <div class="row"><span class="h">Today</span><span>Tokyo opens at 9:00 after Wall Street's rout · <b>22:30 JST — U.S. October jobs report</b> · Mississippi Senate count continues</span></div>
    <div class="row"><span class="h">Ahead</span><span>Mon 9 — COP31 climate summit opens in Antalya · Nov 10, 13, 18 — Alaska count updates (<b>18th: ranked-choice tally</b>) · <b>Dec 17 — Bank of England</b> · Dec — Bank of Japan hike expected</span></div>
  </div>
  <div>
    <div class="bar" style="margin-bottom:2mm;">Top Story</div>
    <h2 class="hd" style="font-size:21pt;">AI Stocks Crash: Wall Street's Worst Day Since April 2025</h2>
    <div class="meta"><span class="st">★★★☆ C1</span><span>MARKETS · FULL REPORT, PAGES 3 AND 5</span></div>
    <div class="body cols2 dc">
      <p class="f"><span class="loc">NEW YORK —</span> American stocks suffered a <span class="w">rout</span> on Thursday as a sell-off in artificial-intelligence and chip companies <span class="w">erased</span> the previous day's rally. The S&amp;P 500 fell 4.4% to 7,353.73, its worst day since the April 2025 tariff sell-off, the Associated Press reported. The Nasdaq lost 5.5% and is now about 12% below last month's record; the Dow dropped 1,833 points. The chip index fell 12%.</p>
      <p><b>Why it matters:</b> Tokyo opens at 9:00 this morning, after a night its market did not see. South Korea's Kospi fell 5.3% and the Nikkei 1.8% even before Wall Street opened.</p>
    </div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);border-top:1.5pt solid #000;border-bottom:1.5pt solid #000;font-family:var(--sans);font-size:9pt;line-height:1.3;">
    <div style="padding:.7mm 2.2mm;border-right:1pt solid #000;border-bottom:1pt solid #000;"><b>POLITICS &amp; WORLD · p.2</b><br>Congress flips · Iran war · Tokyo</div>
    <div style="padding:.7mm 2.2mm;border-right:1pt solid #000;border-bottom:1pt solid #000;"><b>MARKETS · p.3</b><br>AI rout · BoE hike · movers</div>
    <div style="padding:.7mm 2.2mm;border-bottom:1pt solid #000;"><b>SCIENCE &amp; TECH · p.4</b><br>Muscle repair · new crystals</div>
    <div style="padding:.7mm 2.2mm;border-right:1pt solid #000;"><b>SOCIETY &amp; SPORTS · p.4</b><br>School commutes · films · Europe</div>
    <div style="padding:.7mm 2.2mm;border-right:1pt solid #000;"><b>DEEP DIVE · p.5</b><br>Four theories of the AI rout</div>
    <div style="padding:.7mm 2.2mm;"><b>TODAY'S WORDS · p.6</b><br>20 key words, with meanings</div>
  </div>
  <div class="column" style="flex:1;min-height:0;">
    <div style="display:flex;gap:4mm;align-items:baseline;border-top:2.4pt solid #000;padding-top:1.4mm;"><div class="ttl" style="font-size:17pt;">The Number That Arrives While We Sleep</div><div class="by">The Day's Column · ★★★☆ C1</div></div>
    <div class="body cols2" style="margin-top:1.4mm;">
      <p class="f">Every morning, a number is waiting. It was made overnight, in a city we did not see, by people we will never meet. Today the number is large and red.</p>
      <p>It is tempting to read it as a verdict. But a price is only a crowd's best guess at one moment, and crowds change their minds. Yesterday's rally was the best in three months; today's fall erased it. Neither day was the whole truth.</p>
      <p>The wise habit is old and plain: look at the number, then look away from it. Eat breakfast. Ask what has actually changed in your own life since yesterday. Usually the answer is: very little. <span class="w">Composure</span> is not indifference; it is the decision to let a day be a day.</p>
    </div>
  </div>
  <div class="legend" style="border-top:1pt solid #000;padding-top:1mm;">Stocks: Nov 5 U.S. closes (Yahoo Finance, AP). ACWI: ETF close Nov 5, 4 p.m. ET, with day's range (stockanalysis.com). Nikkei, USD/JPY, GBP/JPY: Nov 5 (Trading Economics; FX snapshots differ by up to 0.2%). Gold: futures (Yahoo Finance). Day's range and sparklines only where a fresh source exists (today: ACWI). ≈ approximate. &nbsp;<b>Difficulty (CEFR, editor's estimate):</b> ★ = A1–B1 · ★★ = B2 · ★★★ = C1 · ★★★★ = C2. &nbsp;<span class="w">Blue underlined bold</span> words are explained on page 6.</div>
  <div class="pfoot"><span>THE MORNING DISPATCH · {DATE}</span><span>Page 1 of {N}</span></div>'''

# ---------------- P2 ----------------
YF="https://finance.yahoo.com/markets/live/stock-market-today-thursday-november-5-dow-sp-500-nasdaq-plunge-chip-stocks-melt-down-193726491.html"
KP="https://www.kiplinger.com/investing/stocks/nasdaq-plunges-1-421-points-in-massive-tech-rout-stock-market-today"
AP1="https://www.wflx.com/2026/11/05/brutal-sell-off-ai-stocks-sends-wall-street-reeling-sp-500-sees-worst-day-since-2025-liberation-day-tariffs/"
AP2="https://spectrumlocalnews.com/us/snplus/business/2026/11/05/stock-market-ai-chip-selloff"
CBS="https://www.cbsnews.com/live-updates/midterm-election-results-2026-democrats-house-senate-trump/"
TE_BOE="https://tradingeconomics.com/united-kingdom/interest-rate"
TE_FX="https://tradingeconomics.com/currencies"
TE_JP="https://tradingeconomics.com/japan/stock-market"
NIP="https://www.nippon.com/en/news/"
p2=f'''{run("POLITICS &amp; WORLD · JAPAN")}
  <div class="bar">Politics &amp; World</div>
  <div>
    <h2 class="hd">Democrats Take Congress; Two Senate Races Still Undecided</h2>
    <div class="meta"><span class="st">★★★☆ C1</span><span>POLITICS · UNITED STATES</span></div>
    <div class="body cols2 dc">
      <p class="f"><span class="loc">WASHINGTON —</span> Democrats won control of the House and the Senate in the November 3 midterms, CBS News reported on Thursday. Its summary says Democrats won at least 54 Senate seats; CBS projects a House majority of 251 to 268 seats. Democrats <span class="w">flipped</span> more than two dozen Republican-held House seats, and in Texas Democrat James Talarico beat Republican Ken Paxton for the Senate.</p>
      <p>Two Senate races are still a <span class="w">toss-up</span>. In Alaska, Republican Dan Sullivan and Democrat Mary Peltola are close, and ranked-choice counting may take time. In Mississippi, Republican Cindy Hyde-Smith and Democrat Scott Colom are separated by a razor-thin margin, with thousands of absentee and "affidavit" ballots still to be counted.</p>
    </div>
    <div class="row2" style="margin-top:1mm;">
      <div class="box thick" style="margin:0;"><div class="bh">What they said (as reported by CBS News)</div>
        <div class="view" style="break-inside:avoid;"><span class="o">Trump</span>Said he "would have won" had he been on the ballot; agreed the Iran war's effect on energy prices was "largely true" as a factor.</div>
        <div class="view" style="break-inside:avoid;"><span class="o">Vance</span>Blamed the losses on the Iran war.</div>
      </div>
      <div class="box" style="margin:0;"><div class="bh">How outlets headlined it</div>
        <div class="view" style="break-inside:avoid;"><span class="o">Variety</span>"Democrats Win House and Senate"</div>
        <div class="view" style="break-inside:avoid;"><span class="o">NBC News</span>"Democrats win control of Congress"</div>
        <div class="view" style="break-inside:avoid;"><span class="o">CBS News</span>"…as Democrats prepare to take Congress, GOP grapples with stunning losses"</div>
        <div class="bd" style="font-size:8.6pt;margin-top:1mm;">Headlines only; we read the CBS report in full.</div>
      </div>
    </div>
    {src((CBS,"CBS News live updates, Nov 5"),("https://www.nbcnews.com/politics/2026-elections/house-results","NBC News"),("https://variety.com/2026/politics/news/midterm-election-results-democrats-win-house-senate-1236938473/","Variety"))}
  </div>
  {HR}
  <div>
    <h2 class="hd mid">Bank of England Blames Iran War as Oil Swings</h2>
    <div class="meta"><span class="st">★★☆☆ B2</span><span>WORLD · MIDDLE EAST AND ENERGY</span></div>
    <div class="body cols2">
      <p class="f">The Bank of England said future interest-rate decisions will depend largely on the Iran war, which has pushed up oil prices and <span class="w">inflation</span> around the world, the Associated Press reported. Governor Andrew Bailey said: "The best thing that can happen is to resolve the conflict in the Middle East; there's no question about it."</p>
      <p>Brent crude fell nearly 9% on Wednesday, then rose 3.9% on Thursday to $98.29. We could not confirm what drove Wednesday's fall.</p>
    </div>
    {src((AP1,"AP via WFLX"),(AP2,"AP via Spectrum News"))}
  </div>
  {HR}
  <div class="bar">Japan</div>
  <div>
    <h2 class="hd mid">Tokyo Faces a Wall Street Hangover at the Open</h2>
    <div class="meta"><span class="st">★★★☆ C1</span><span>JAPAN · MARKETS AND SECURITY</span></div>
    <div class="body cols2">
      <p class="f">The Nikkei 225 fell 1.79% on Thursday to close near 61,078, its fourth straight losing session, Trading Economics reported. Tech shares came under pressure over worries about AI development and possible tighter rules on data-center investment. That session ended before the U.S. sell-off, so today's open is the first chance for Tokyo to react.</p>
      <p>Nippon.com headlines (details unavailable): NTT Docomo faces a massive data <span class="w">breach</span> after a cyberattack; Japan's emergency package will include a "cyber rescue squad"; Prime Minister Takaichi vows to keep cooperating with President Trump (Nov 6).</p>
    </div>
    {src((TE_JP,"Trading Economics"),(NIP,"Nippon.com news index"))}
  </div>
  <div style="flex:1;"></div>
  {foot("Politics &amp; World · Japan",2)}'''

# ---------------- P3 ----------------
p3=f'''{run("MARKETS &amp; ECONOMY")}
  <div class="bar">Markets &amp; Economy</div>
  <div>
    <h2 class="hd">The AI Trade Cracks: Chip Stocks Plunge, Fear Gauge Jumps 70%</h2>
    <div class="meta"><span class="st">★★★☆ C1</span><span>MARKETS · WALL STREET, THURSDAY NOV 5</span></div>
    <div class="row2 r6040">
      <div class="body dc" style="text-align:justify;">
        <p class="f">All three major U.S. indexes fell sharply, and <span class="w">volatility</span> soared. The Philadelphia chip index lost 12.25% and the VIX jumped to 28.18. Retail investors were heavy sellers: Vanda Research said they sold a net $358 million of U.S. stocks, their heaviest day since 2020, which Vanda's Viraj Patel called "a total <span class="w">capitulation</span> by retail investors."</p>
      </div>
      <table class="t">
        <tr><th>INDEX / ASSET</th><th class="r">CLOSE</th><th class="r">CHANGE</th></tr>
        <tr><td>Dow</td><td class="r">51,523.06</td><td class="r dn">−3.44%</td></tr>
        <tr><td>S&amp;P 500</td><td class="r">7,353.73</td><td class="r dn">−4.36%</td></tr>
        <tr><td>Nasdaq</td><td class="r">24,315.00</td><td class="r dn">−5.52%</td></tr>
        <tr><td>Chip index (SOX)</td><td class="r">9,011.14</td><td class="r dn">−12.25%</td></tr>
        <tr><td>10-yr yield</td><td class="r">4.84%</td><td class="r">from 4.90%</td></tr>
      </table>
    </div>
    <div class="box thick" style="margin-top:2mm;"><div class="bh">Why did stocks fall? Outlets and analysts differ</div>
      <div class="cols2" style="column-gap:5mm;">
        <div class="view" style="break-inside:avoid;"><span class="o">AP</span>Worries that AI data-center building may slow because borrowing costs rose; critics say AI prices are in a bubble; Democratic gains raised the chance governments pause data-center construction.</div>
        <div class="view" style="break-inside:avoid;"><span class="o">Kiplinger</span>Fear that Democratic leadership could slow the data-center buildout; valuations "disconnected from fundamentals"; profit-taking on this year's biggest gainers.</div>
        <div class="view" style="break-inside:avoid;"><span class="o">Yahoo Finance</span>Institutions reportedly sold 2026's top performers to lock in gains. Nomura's Charlie McElligott: "They're shooting the generals."</div>
      </div>
    </div>
    {src((YF,"Yahoo Finance live blog"),(KP,"Kiplinger"),(AP1,"AP via WFLX"),(AP2,"AP via Spectrum News"))}
  </div>
  {HR}
  <div>
    <h2 class="hd mid">Stocks of the Day: Chips Plummet, AppLovin Soars 31%</h2>
    <div class="meta"><span class="st">★★★☆ C1</span><span>MARKETS · INDIVIDUAL STOCKS</span></div>
    <div class="row2 r4060">
      <table class="t">
        <tr><th>STOCK</th><th class="r">MOVE</th></tr>
        <tr><td>AppLovin</td><td class="r up">+31%</td></tr>
        <tr><td>Tapestry</td><td class="r up">+7.1%</td></tr>
        <tr><td>Sandisk</td><td class="r dn">−22.3%</td></tr>
        <tr><td>Micron</td><td class="r dn">−17.5%</td></tr>
        <tr><td>AMD</td><td class="r dn">−17.3%</td></tr>
        <tr><td>Nvidia</td><td class="r dn">−9.3%</td></tr>
      </table>
      <div class="body">
        <p class="f"><b>Nvidia</b> was the biggest drag on the S&amp;P 500, a day after a 3.2% fall. Chip makers <span class="w">plummeted</span> across the board. <b>AppLovin</b> bucked the trend: it beat revenue and profit expectations and approved up to $3.2 billion in share <span class="w">buybacks</span>. <b>Tapestry</b> rose after stronger-than-expected profit and a raised forecast. Thursday closes (AP, Kiplinger); Yahoo Finance put AMD near −15%.</p>
      </div>
    </div>
  </div>
  {HR}
  <div>
    <h2 class="hd mid">Pound and Yen: Bank of England Raises Rates to 4%</h2>
    <div class="meta"><span class="st">★★★☆ C1</span><span>MARKETS · CENTRAL BANKS AND CURRENCIES</span></div>
    <div class="body cols2">
      <p class="f">The Bank of England raised its main rate by 0.25 points to 4.00%, its first <span class="w">hike</span> since August 2023, by 8 votes to 1. Catherine Mann <span class="w">dissented</span>, preferring 0.5 points. The bank expects inflation to rise to about 5% by mid-next year, from 3.5%. The next decision is on December 17.</p>
      <p><b>For GBP/JPY holders:</b> Trading Economics quoted GBP/JPY near 212.95, down 0.23%, on Thursday (its own text said 213.04, down 0.19%, so treat it as about 213). InvestingLive's headline said sterling "struggles to hold its gains" after the decision.</p>
    </div>
    {src((TE_BOE,"Trading Economics: BoE"),(TE_FX,"Trading Economics: currencies"),("https://investinglive.com/","InvestingLive"))}
  </div>
  <div style="flex:1;"></div>
  {foot("Markets &amp; Economy",3)}'''

# ---------------- P4 ----------------
SD="https://www.sciencedaily.com/news/top/science/"
TN="https://www.the-numbers.com/box-office-chart/weekend/2026/10/30"
p4=f'''{run("SCIENCE · SOCIETY · CULTURE · SPORTS")}
  <div class="bar">Science &amp; Technology</div>
  <div>
    <h2 class="hd mid">A "Super" Muscle Protein Could Help Ageing Bodies Repair Themselves</h2>
    <div class="meta"><span class="st">★★☆☆ B2</span><span>SCIENCE · HEALTH · REPORTED NOV 4</span></div>
    <div class="body cols2 dc">
      <p class="f">Researchers report a compound that turns a muscle-repair protein into a stronger version, nicknamed "Super HGF." The upgraded protein binds to its receptor far better and can <span class="w">resist</span> damage linked to ageing, according to ScienceDaily's summary. The work is at an early stage; the page we read did not name the institution or say whether it has been tested in people.</p>
    </div>
  </div>
  <div class="row2">
    <div>
      <h2 class="hd sm">MIT Breaks a 20-Year Rule to Build New Crystals</h2>
      <div class="meta"><span class="st">★★★☆ C1</span><span>TECH · MATERIALS</span></div>
      <div class="body"><p class="f">MIT scientists found that flexible molecular links, not <span class="w">rigid</span> ones, let nanoparticles arrange themselves into never-before-seen crystal structures.</p></div>
    </div>
    <div>
      <h2 class="hd sm">Why Brains Are Cross-Wired</h2>
      <div class="meta"><span class="st">★★★☆ C1</span><span>SCIENCE · BRAIN</span></div>
      <div class="body"><p class="f">Researchers propose that the crossing of the brain's connections to opposite sides of the body arose more than 500 million years ago. It is a hypothesis, not a settled finding.</p></div>
    </div>
  </div>
  {src((SD,"ScienceDaily top science, Nov 4 headlines"))}
  {HR}
  <div class="bar">Society, Culture &amp; Sports</div>
  <div class="row2">
    <div>
      <h2 class="hd sm">Permanent Daylight Time Would Put Children on Dark Roads</h2>
      <div class="meta"><span class="st">★☆☆☆ B1</span><span>SOCIETY · UNITED STATES</span></div>
      <div class="body"><p class="f">A new study estimates that permanent daylight saving time would add at least 2 billion school <span class="w">commutes</span> in the dark for American children. Scientists warn of a "dark side" to the idea.</p></div>
    </div>
    <div>
      <h2 class="hd sm">"You Can See Everything" Tops the Box Office</h2>
      <div class="meta"><span class="st">★★☆☆ B2</span><span>CULTURE · FILM</span></div>
      <div class="body"><p class="f">The film earned $11.4 million for the weekend and $64.7 million in total. Its <span class="w">gross</span> narrowly beat "Clayface" ($11.0 million) and "Wildwood" ($8.9 million). This is the latest chart we could find; Nov 6 numbers are not out yet.</p></div>
    </div>
  </div>
  {src((SD,"ScienceDaily"),(TN,"The Numbers"))}
  {HR}
  <div>
    <h2 class="hd mid">Champions League: Liverpool Lose in Istanbul as Arsenal and City Win</h2>
    <div class="meta"><span class="st">★★☆☆ B2</span><span>SPORTS · FOOTBALL · MATCHES OF NOV 3–4</span></div>
    <div class="row2 r6040">
      <div class="body">
        <p class="f">Fenerbahçe beat Liverpool 3–2 in Istanbul, an <span class="w">upset</span>. Arsenal won 2–1 at Slavia Prague and Manchester City won 3–2 at RB Leipzig. Real Madrid won 3–2 at AEK Athens. Como thrashed Lens 9–1, and Paris Saint-Germain won 6–0 at Villarreal.</p>
        <p style="text-indent:1.2em;margin-top:1mm;"><b>NBA, Nov 4:</b> Knicks 135–105 Bulls; Lakers 116–103 Kings; Celtics 109–102 Bucks.</p>
      </div>
      <table class="t">
        <tr><th>MATCH (NOV 4)</th><th class="r">SCORE</th></tr>
        <tr><td>Fenerbahçe v Liverpool</td><td class="r">3–2</td></tr>
        <tr><td>Slavia Prague v Arsenal</td><td class="r">1–2</td></tr>
        <tr><td>RB Leipzig v Man City</td><td class="r">2–3</td></tr>
        <tr><td>AEK v Real Madrid</td><td class="r">2–3</td></tr>
        <tr><td>Porto v Napoli</td><td class="r">4–1</td></tr>
        <tr><td>Lens v Como</td><td class="r">1–9</td></tr>
      </table>
    </div>
    <div class="src"><b>Source:</b> SportRadar match data, retrieved Nov 6 (JST).</div>
  </div>
  <div style="flex:1;"></div>
  {foot("Science · Society · Culture · Sports",4)}'''

# ---------------- P5 DEEP DIVE ----------------
p5=f'''{run("DEEP DIVE")}
  <div class="bar">Deep Dive</div>
  <div>
    <h2 class="hd big" style="font-size:25pt;">Four Theories of the AI Rout</h2>
    <div class="deck">One-day moves invite certainty. The evidence supports the size of the fall, not a single cause.</div>
    <div class="meta"><span class="st">★★★☆ C1</span><span>MARKETS · ANALYSIS</span></div>
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);border-top:1.5pt solid #000;border-bottom:1.5pt solid #000;font-family:var(--sans);text-align:center;">
    <div style="padding:1mm;border-right:1pt solid #000;"><div style="font-size:8.2pt;font-weight:800;">S&amp;P 500, THU</div><div style="font-size:17pt;font-weight:900;font-family:var(--serif);">−4.36%</div><div style="font-size:8pt;">worst since Apr 2025</div></div>
    <div style="padding:1mm;border-right:1pt solid #000;"><div style="font-size:8.2pt;font-weight:800;">NASDAQ vs RECORD</div><div style="font-size:17pt;font-weight:900;font-family:var(--serif);">−11.9%</div><div style="font-size:8pt;">record set last month</div></div>
    <div style="padding:1mm;border-right:1pt solid #000;"><div style="font-size:8.2pt;font-weight:800;">CHIP INDEX (SOX)</div><div style="font-size:17pt;font-weight:900;font-family:var(--serif);">−12.25%</div><div style="font-size:8pt;">one day</div></div>
    <div style="padding:1mm;"><div style="font-size:8.2pt;font-weight:800;">VIX</div><div style="font-size:17pt;font-weight:900;font-family:var(--serif);">28.18</div><div style="font-size:8pt;">up 69.7%</div></div>
  </div>
  <div class="body cols2">
    <p class="f"><b>What happened</b></p>
    <ul>
      <li>Thursday's sell-off wiped out Wednesday's gains, which had been the S&amp;P 500's best day in three months (AP).</li>
      <li>The Nasdaq entered a <span class="w">correction</span>: more than 10% below its Oct 6 record of 27,599.79 (Kiplinger).</li>
      <li>Nvidia fell 9.3%, AMD 17.3%, Micron 17.5%; yet about two in five S&amp;P 500 stocks still rose at midday (AP).</li>
      <li>Kospi −5.3% and Nikkei −1.8% earlier in Asia; FTSE 100 −0.4% (AP).</li>
    </ul>
    <p><b>What to watch</b></p>
    <ul>
      <li>Tokyo's 9:00 open and Asia's reaction.</li>
      <li>The U.S. jobs report at 22:30 JST today.</li>
      <li>Whether borrowing costs keep easing: the 10-year yield fell to 4.84% from above 5.30% last month (AP).</li>
    </ul>
  </div>
  <table class="t tl">
    <tr><th>DATE</th><th>EVENT</th></tr>
    <tr><td>Oct 6</td><td>Nasdaq Composite hits its record high, 27,599.79 (Kiplinger).</td></tr>
    <tr><td>Oct</td><td>10-year Treasury yield above 5.30% at some point last month (AP).</td></tr>
    <tr><td>Nov 3</td><td>U.S. midterms; Democrats win control of Congress (CBS). 10-year yield 4.95% on election night (AP).</td></tr>
    <tr><td>Nov 4</td><td>S&amp;P 500's best day in three months; Brent falls nearly 9% (AP).</td></tr>
    <tr><td>Nov 5</td><td>Chip and AI stocks crash; Bank of England raises rates to 4%.</td></tr>
  </table>
  <table class="t">
    <tr><th style="width:21%;">THEORY</th><th style="width:44%;">WHO SAYS IT, AND WHAT THEY SAY</th><th>WHAT IS UNKNOWN</th></tr>
    <tr><td><b>1. Politics</b></td><td>AP and Kiplinger: Democratic wins raise the chance that governments slow data-center construction, cutting demand for chips and power.</td><td>No policy has been announced in the reports we read; this is an expectation.</td></tr>
    <tr><td><b>2. Borrowing costs</b></td><td>AP: AI data-center building may slow because borrowing became more expensive.</td><td>Yields fell on Thursday (AP), which sits awkwardly with a rates-only story.</td></tr>
    <tr><td><b>3. Valuation</b></td><td>AP: critics say AI stocks rose too high. Bahnsen (Kiplinger): valuations "remain way too high."</td><td>Valuation does not say why the fall came on this day.</td></tr>
    <tr><td><b>4. Positioning</b></td><td>Yahoo Finance: institutions reportedly sold 2026's top performers to lock in gains; Vanda: retail sold a net $358M.</td><td>"Reportedly": we could not see the underlying data.</td></tr>
  </table>
  <div class="box thick" style="margin:0;"><div class="bh">Editor's assessment: what the evidence supports and what it does not (analysis, not news)</div>
    <div class="bd"><ul style="margin:0 0 0 4.5mm;">
      <li><b>Supported:</b> the scale of the fall, its concentration in chip stocks (−12%), and that retail and institutional selling were both reported.</li>
      <li><b>Not supported:</b> any single cause. The election link is the explanation of commentators, not a measured fact, and mixed moves (AppLovin +31%) show the sell-off was not uniform.</li>
      <li><b>Cautions:</b> a <span class="w">valuation</span> argument and a <span class="w">profit-taking</span> argument can both be true at once. We offer no forecast and no investment advice.</li>
    </ul></div>
  </div>
  {src((YF,"Yahoo Finance"),(KP,"Kiplinger"),(AP1,"AP via WFLX"),(AP2,"AP via Spectrum News"),(CBS,"CBS News"))}
  <div style="flex:1;"></div>
  {foot("Deep Dive",5)}'''

# ---------------- P6 WORDS ----------------
V=[
("rout","C1","大敗、(相場の)総崩れ","The S&amp;P 500 suffered a rout on Thursday."),
("erase","B2","消し去る","…a sell-off erased the previous day's rally."),
("composure","C1","落ち着き、冷静さ","Composure is not indifference."),
("flip","B2","(議席などを)奪う、ひっくり返す","Democrats flipped more than two dozen seats."),
("toss-up","C1","どちらとも言えない接戦","Two Senate races are still a toss-up."),
("inflation","B2","インフレ、物価上昇","…pushed up oil prices and inflation."),
("breach","C1","(情報)流出、違反","NTT Docomo faces a massive data breach."),
("volatility","C1","(価格の)変動の激しさ","Volatility soared."),
("capitulation","C2","(投げ売りによる)総降参","…a total capitulation by retail investors."),
("plummet","C1","急落する","Chip makers plummeted across the board."),
("buyback","C1","自社株買い","…up to $3.2 billion in share buybacks."),
("hike","B2","(金利の)引き上げ","…its first hike since August 2023."),
("dissent","C1","反対意見を述べる","Catherine Mann dissented."),
("resist","B2","抵抗する、耐える","…can resist damage linked to ageing."),
("rigid","C1","硬い、柔軟性のない","Flexible links, not rigid ones…"),
("commute","B2","通勤・通学(の道のり)","…2 billion school commutes in the dark."),
("gross","C1","総興行収入","Its gross narrowly beat \"Clayface\"."),
("upset","B2","(スポーツの)番狂わせ","Fenerbahçe's win was an upset."),
("correction","C1","(株価の)調整局面(10%超の下落)","The Nasdaq entered a correction."),
("valuation","C1","(株式などの)評価額、株価水準","A valuation argument and a profit-taking one…"),
("profit-taking","C1","利益確定売り","…profit-taking on this year's biggest gainers."),
]
rows=''.join(f'<tr><td class="w1">{w}</td><td class="lv">{l}</td><td><span class="jp">{jp}</span><br><i>{ex}</i></td></tr>' for w,l,jp,ex in V)
half=(len(V)+1)//2
def tbl(rs): return '<table class="t vocab"><tr><th>WORD</th><th>CEFR</th><th>MEANING · EXAMPLE FROM THIS ISSUE</th></tr>'+rs+'</table>'
def rowsof(lst): return ''.join(f'<tr><td class="w1">{w}</td><td class="lv">{l}</td><td><span class="jp">{jp}</span><br><i>{ex}</i></td></tr>' for w,l,jp,ex in lst)
p6=f'''{run("TODAY'S WORDS")}
  <div class="bar">Today's Words</div>
  <div class="row2">{tbl(rowsof(V[:half]))}{tbl(rowsof(V[half:]))}</div>
  <div class="box thick" style="margin:0;"><div class="bh">About this edition</div>
    <div class="bd"><ul style="margin:0 0 0 4.5mm;">
      <li><b>Plan B edition:</b> the scheduled run failed this morning (no access to the template). This issue was built by hand on the morning of Nov 6 (JST) from a lighter 6-page plan, in the new classic layout (no boxed articles, drop caps).</li>
      <li><b>Market numbers:</b> U.S. closes are from Yahoo Finance and the AP (two sources agree on the index levels). ACWI is the 4 p.m. ET close from stockanalysis.com (an earlier snapshot we saw, $152.05, was replaced by this final figure). USD/JPY, GBP/JPY and the Nikkei level come from Trading Economics (one source; its snapshots differ slightly, so ≈). Gold is a futures price. Day's range appears only for ACWI and sparklines are omitted: the free data pages we can reach were days old or blocked. TOPIX was not retrieved.</li>
      <li><b>Not confirmed:</b> the reason oil fell about 9% on Wednesday; details of the Docomo breach, the emergency package and Takaichi's remarks (we saw headlines only); where the "Super HGF" research was done.</li>
      <li><b>Thin sections:</b> science and culture rely on single summary pages; the culture item is from the box-office chart dated Oct 30. Outlet "framing" boxes use only headlines or statements we actually read.</li>
    </ul></div>
  </div>
  <div style="flex:1;"></div>
  {foot("Today's Words",6)}'''

html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>The Morning Dispatch — Nov 6, 2026</title><link rel="stylesheet" href="../assets/style.css"></head><body>
'''+''.join(page(i+1,b) for i,b in enumerate([p1,p2,p3,p4,p5,p6]))+'</body></html>'
# vocab consistency check
used=set(re.findall(r'<span class="w">([^<]+)</span>',html))
listed={w for w,_,_,_ in V}
norm=lambda s:s.lower()
print("used not listed:",sorted({u for u in used if not any(u.lower().startswith(l[:5]) for l in listed)}))
print("listed not used:",sorted({l for l in listed if not any(u.lower().startswith(l[:5]) for u in used)}))
pathlib.Path('/home/claude/newspaper/work/issue.html').write_text(html)
print("ok",len(html))

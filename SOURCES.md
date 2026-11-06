# Source list for The Morning Dispatch (tested 2026-11-06)

Check these FIRST, in this order, before open-ended searching. WebFetch one page per site at a time (parallel fetches to the same site get rate-limited).

## Markets and FX (always)
- ACWI ETF close + daily change: https://stockanalysis.com/stocks/acwi/ (works; history page lags, don't rely on it)
- FX, rates, Nikkei level: https://tradingeconomics.com/currencies , https://tradingeconomics.com/japan/stock-market , https://tradingeconomics.com/united-kingdom/interest-rate (GBP/JPY is NOT listed; compute from GBP/USD and USD/JPY and mark "calculated")
- U.S. close, oil, gold, VIX, yields: WebSearch "stock market today <weekday> <month> <day> Dow S&P 500 Nasdaq" -> open the Yahoo Finance live blog (finance.yahoo.com/markets/live/...) and Kiplinger "stock market today"; cross-check index levels with an AP story (often republished by local TV sites such as wflx.com, spectrumlocalnews.com).
- Gold/WTI/Brent: take from the same Yahoo/AP pages; state whether futures or spot.

## World and politics
- AP wire via local-station republishers (search "AP <topic> <date>"); CBS News live-updates pages (cbsnews.com/live-updates/...) work well; NBC News, Variety live blogs for headlines.
## Japan
- https://www.nippon.com/en/news/ (headlines with dates only; open the article via WebSearch for details). Also search "Kyodo", "NHK World", "Japan Times" + topic.
## Science
- https://www.sciencedaily.com/news/top/science/ (dated headlines + one-line findings)
## Culture
- Box office: https://www.the-numbers.com/box-office-chart/weekend/YYYY/MM/DD (use the latest Friday date)
## Sports
- Use the fetch_sports_data tool (champions_league, nba, nfl, epl, mlb, tennis...) -- fast and reliable.

## Known bad / stale (skip)
- bbc.com: blocked. ms.now: fails. cnbc.com and asia.nikkei.com home pages: stale cached copies from years ago (use dated article URLs from WebSearch instead). livescience tag pages and japantoday.com home: stale or undated.
- General WebSearch often returns last year's articles: always include the full date ("November 5 2026") and check the article date before using it.

## Rules
- Prefer two sources for every number; when only one, mark "≈" and say so in "About this edition".
- Never present an undated or old page as today's news.

## Reader's media list and what actually opens (tested 2026-11-06)
Opens (homepage/index, use for headlines; open dated articles via WebSearch for detail): Al Jazeera (aljazeera.com), SCMP (scmp.com; relative timestamps), investingLive (investinglive.com; dated headlines, FX/market color), FXStreet news (no timestamps), CBS News, Yahoo Finance live blogs, Kiplinger, Trading Economics, stockanalysis.com quote pages, Nippon.com.
Blocked by the fetch tool (do not retry; use WebSearch snippets/headlines only, or AP/Reuters text republished by local sites): apnews.com, reuters.com, thehindu.com, theguardian.com, bbc.com.
Not yet tested: Ground News, NYT, WSJ, Fox, CNN, Globe and Mail, Asia Times, Times of India, Indian Express, Bloomberg, FT, Forbes, Foreign Affairs, Forex Factory, TradingView, Myfxbook, CME FedWatch, BLS, BEA, ECB, Yomiuri, Sankei, Asahi, Mainichi, Nikkei. Paywalled sites (NYT, WSJ, FT, Bloomberg) are never bypassed: use headlines/snippets only and say so.
Price data: no API works (Yahoo chart/Stooq robots-disallowed). Fresh: stockanalysis.com/stocks/<ticker>/ (price, close, day range, prev close). TE currency pages give price/change, no range.

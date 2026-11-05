"""Usage: python3 tools/fit.py work/issue.html  -> prints per-page need vs 277mm (must be <=277)."""
import sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve()
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(); pg.goto(src.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(700)
    pg.add_style_tag(content=".content{display:block !important;} .content>*{flex:none !important;}")
    pg.wait_for_timeout(300)
    r = pg.evaluate("""()=>[...document.querySelectorAll('.page')].map((p,i)=>{
      const mm=x=>x*25.4/96; const kids=[...p.querySelector('.content').children];
      const sum=kids.reduce((s,k)=>s+mm(k.getBoundingClientRect().height),0);
      return {n:i+1, need:Math.round((sum+2.6*(kids.length-1))*10)/10};})""")
    for x in r:
        d = x['need'] - 277
        print(f"page {x['n']}: need {x['need']} mm ->", f"OVER by {d:.1f}" if d > 0 else f"ok, spare {-d:.1f} (fill {x['need']/277*100:.0f}%)")
    print("pages:", len(r)); b.close()

"""Usage: python3 tools/render.py work/issue.html out/MorningDispatch_YYYY-MM-DD.pdf"""
import sys, pathlib
from playwright.sync_api import sync_playwright
src = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]); out.parent.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(); pg.goto(src.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(700)
    pg.pdf(path=str(out), format="A4", print_background=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
    b.close()
print("wrote", out)

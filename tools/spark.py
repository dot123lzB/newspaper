"""Tiny inline-SVG helpers for market cells (no invented data: only call with verified numbers).
  rangebar(low, high, close)  -> Day's Range line + a thin bar with a tick at the close
  spark(series)               -> sparkline polyline from >=4 verified closes (oldest->newest)
Both return HTML/SVG strings to paste into a .mkt .c cell. Return '' when inputs are missing."""
def rangebar(low, high, close, fmt="{:,.2f}", w=96, h=9):
    if None in (low, high, close) or high <= low: return ""
    x = (close - low) / (high - low) * (w - 4) + 2
    svg = (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><line x1="2" y1="{h/2}" x2="{w-2}" y2="{h/2}" stroke="#000" stroke-width="1.2"/>'
           f'<line x1="2" y1="1" x2="2" y2="{h-1}" stroke="#000" stroke-width="1"/><line x1="{w-2}" y1="1" x2="{w-2}" y2="{h-1}" stroke="#000" stroke-width="1"/>'
           f'<rect x="{x-2.2:.1f}" y="1.5" width="4.4" height="{h-3}" fill="#000"/></svg>')
    return f'<div class="rng">Range {fmt.format(low)} – {fmt.format(high)}{svg}</div>'
def spark(series, w=96, h=16, color="#000"):
    s = [v for v in series if v is not None]
    if len(s) < 4: return ""
    lo, hi = min(s), max(s); span = (hi - lo) or 1
    pts = " ".join(f"{i*(w-4)/(len(s)-1)+2:.1f},{h-2-(v-lo)/span*(h-4):.1f}" for i, v in enumerate(s))
    ex, ey = pts.split()[-1].split(",")
    return (f'<svg class="spark" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><polyline points="{pts}" fill="none" stroke="{color}" stroke-width="1.5"/>'
            f'<circle cx="{ex}" cy="{ey}" r="2" fill="{color}"/></svg>')

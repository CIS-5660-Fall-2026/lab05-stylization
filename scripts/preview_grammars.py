from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "assets"
OUT.mkdir(exist_ok=True)
FONT = 'C:/Windows/Fonts/arial.ttf'

def tokens(text):
    result = []
    i = 0
    while i < len(text):
        c = text[i]
        i += 1
        if c.isspace():
            continue
        arg = None
        if i < len(text) and text[i] == '(':
            end = text.index(')', i)
            arg = float(text[i+1:end])
            i = end + 1
        result.append((c, arg))
    return result

def fern_tokens(n):
    seq = [('A', 1.0)]
    for _ in range(n):
        nxt = []
        for c, l in seq:
            if c == 'A':
                nxt += tokens(f'F({l})[+(65)B({l*1.4})][-(65)B({l*1.4})]-(1.2)A({l*.94})')
            elif c == 'B':
                nxt += tokens(f'F({l*.32})[+(55)C({l*.5})][-(55)C({l*.5})]B({l*.85})')
            elif c == 'C':
                nxt += tokens(f'{{. +(25)f({l*.55}). -(50)f({l*.55}). -(130)f({l*.55}). -(50)f({l*.55}).}}')
            else:
                nxt.append((c, l))
        seq = nxt
    return seq

def puzzle_tokens(premise, rule, n):
    for _ in range(n):
        premise = premise.replace('F', rule)
    return tokens(premise)

def turtle(seq, angle=20):
    x, y, heading = 0., 0., 90.
    stack, lines, polys = [], [], []
    poly = None
    for c, arg in seq:
        if c in 'Ff':
            distance = 1 if arg is None else arg
            nx = x + distance * math.cos(math.radians(heading))
            ny = y + distance * math.sin(math.radians(heading))
            if c == 'F':
                lines.append(((x, y), (nx, ny)))
            x, y = nx, ny
        elif c == '+':
            heading -= angle if arg is None else arg
        elif c == '-':
            heading += angle if arg is None else arg
        elif c == '[':
            stack.append((x, y, heading))
        elif c == ']':
            x, y, heading = stack.pop()
        elif c == '{':
            poly = []
        elif c == '.':
            if poly is not None:
                poly.append((x, y))
        elif c == '}':
            polys.append(poly)
            poly = None
    assert not stack and poly is None
    return lines, polys

def render(draw, bounds, lines, polys, color=(25, 32, 30), line_width=2):
    points = [p for l in lines for p in l] + [p for poly in polys for p in poly]
    mnx, mxx = min(p[0] for p in points), max(p[0] for p in points)
    mny, mxy = min(p[1] for p in points), max(p[1] for p in points)
    x0,y0,x1,y1 = bounds
    scale = min((x1-x0)/max(mxx-mnx,.01), (y1-y0)/max(mxy-mny,.01))
    cx,cy=(x0+x1)/2,(y0+y1)/2
    def p(pos):
        return (cx+(pos[0]-(mnx+mxx)/2)*scale, cy-(pos[1]-(mny+mxy)/2)*scale)
    for poly in polys:
        draw.polygon([p(pt) for pt in poly], fill=(60,119,73), outline=(41,83,54))
    for a,b in lines:
        draw.line([p(a),p(b)], fill=color,width=line_width)

def main():
    im=Image.new('RGB',(1500,1560),(248,249,245))
    d=ImageDraw.Draw(im)
    title=ImageFont.truetype(FONT,28)
    small=ImageFont.truetype(FONT,20)
    for row,(label,ns) in enumerate([('WHEAT',(1,2,3)),('SQUARE',(1,2,3)),('FERN',(4,8,14))]):
        for col,n in enumerate(ns):
            if row==0:
                geo=turtle(puzzle_tokens('F','FF[-FF]F[-FF]FF-',n))
                assert len(geo[0])==9**n
            elif row==1:
                geo=turtle(puzzle_tokens('+(90)F','F+F-F-F+F',n),90)
                assert len(geo[0])==5**n
            else:
                geo=turtle(fern_tokens(n))
            x0,y0=col*500,row*500+42
            d.text((x0+26,y0),f'{label} / n = {n}',font=title,fill=(30,54,43))
            render(d,(x0+30,y0+60,x0+470,y0+454),*geo)
            print(label,n,len(geo[0]),len(geo[1]))
    d.text((25,1520),'Independent grammar preview - NOT a Houdini screenshot; Houdini verification pending.',font=small,fill=(78,88,81))
    im.save(OUT/'grammar_preview.png')

if __name__=='__main__':
    main()

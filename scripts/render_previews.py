"""Generate labeled PNG previews and static OBJ geometry. Requires Pillow."""

import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from lsystem import ROOT, geometry, load_config, write_obj

SCALE = 2


def font(size):
    for name in ("/System/Library/Fonts/Supplemental/Arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size * SCALE)
        except OSError:
            pass
    return ImageFont.load_default(size=size * SCALE)


def bounds(lines, polygons):
    points = [p for start, end, _ in lines for p in (start, end)]
    points += [p for polygon in polygons for p in polygon]
    xs, ys = zip(*points)
    return min(xs), min(ys), max(xs), max(ys)


def gallery(key, config, geometries):
    width, height = 1560, 820
    canvas = Image.new("RGB", (width * SCALE, height * SCALE), "#f6f5f0")
    draw = ImageDraw.Draw(canvas)

    def text(x, y, label, size=20, fill="#25352b"):
        draw.text((x * SCALE, y * SCALE), label, fill=fill, font=font(size))

    text(44, 30, config["title"], 34)
    text(44, 80, "Parallel rewriting / deterministic 2D geometry", 18, "#69736a")
    all_bounds = [bounds(*item) for item in geometries]
    shared = min(430 / max(b[2] - b[0], 0.001) for b in all_bounds)
    shared = min(shared, min(530 / (b[3] - b[1]) for b in all_bounds))
    for column, (generation, (lines, polygons), b) in enumerate(zip(config["generations"], geometries, all_bounds)):
        x0 = 30 + column * 510
        draw.rounded_rectangle((x0*SCALE, 124*SCALE, (x0+490)*SCALE, 725*SCALE),
                               radius=14*SCALE, fill="white", outline="#d8ded7", width=SCALE)
        text(x0+24, 142, f"n = {generation}", 24)
        scale = shared if key == "fern" else min(430/max(b[2]-b[0], 0.001), 490/(b[3]-b[1]))
        center_x = (b[0] + b[2])/2
        baseline = 683 if key == "fern" else (190+683)/2 + (b[3]-b[1])*scale/2

        def point(p):
            return ((x0+245+(p[0]-center_x)*scale)*SCALE,
                    (baseline-(p[1]-b[1])*scale)*SCALE)

        for polygon in polygons:
            draw.polygon([point(p) for p in polygon], fill="#579545")
        for start, end, line_width in lines:
            stroke = max(0.65, line_width*scale) if key == "fern" else 1.35
            draw.line((point(start), point(end)), fill="#2c5134" if key=="fern" else "#26362d",
                      width=max(1, round(stroke*SCALE)))
        text(x0+24, 698, f"{len(lines)} segments" + (f" / {len(polygons)} blades" if polygons else ""), 13, "#69736a")
    text(44, 751, "Python preview from the supplied rules; native results are in images/houdini/.", 17, "#69736a")
    text(44, 780, "Common scale across fern iterations." if key=="fern" else "Each puzzle iteration is fitted independently, as in the assignment.", 15, "#69736a")
    canvas.resize((width, height), Image.Resampling.LANCZOS).save(ROOT/"images/previews"/f"{key}-iterations.png")


def main():
    (ROOT/"images/previews").mkdir(exist_ok=True)
    metrics = {"renderer": "Python 2D subset; not Houdini", "models": {}}
    for key, config in load_config().items():
        geometries = []
        metrics["models"][key] = {}
        for generation in config["generations"]:
            lines, polygons = geometry(config, generation)
            geometries.append((lines, polygons))
            write_obj(ROOT/"geometry"/f"{key}-n{generation:02d}.obj", lines, polygons)
            metrics["models"][key][str(generation)] = {"segments": len(lines), "blades": len(polygons)}
        gallery(key, config, geometries)
    (ROOT/"geometry/metrics.json").write_text(json.dumps(metrics, indent=2)+"\n")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()

"""Check grammar geometry, exported topology, and local README links."""

import math
import re
from lsystem import ROOT, expand, geometry, load_config


def close(point, expected):
    assert all(math.isclose(a, b, abs_tol=1e-8) for a, b in zip(point, expected)), (point, expected)


def main():
    configs = load_config()
    wheat, _ = geometry(configs["wheat"], 1)
    close(wheat[-1][1], (0, 5))
    close(wheat[2][0], (0, 2))
    close(wheat[3][1], (-2*math.sin(math.radians(20)), 2+2*math.cos(math.radians(20))))
    close(wheat[5][0], (0, 3))
    wheat2, _ = geometry(configs["wheat"], 2)
    # The terminal turn must affect following rewritten blocks, not be discarded.
    close(wheat2[-1][1], (sum(5*math.sin(math.radians(-20*k)) for k in range(5)),
                          sum(5*math.cos(math.radians(-20*k)) for k in range(5))))
    square, _ = geometry(configs["square"], 1)
    expected = [(0,0), (1,0), (1,-1), (2,-1), (2,0), (3,0)]
    for i, (start, end, _) in enumerate(square):
        close(start, expected[i])
        close(end, expected[i+1])

    for key, config in configs.items():
        for n in config["generations"]:
            lines, polygons = geometry(config, n)
            word, _ = expand(config, n)
            if key in ("square", "wheat"):
                assert len(lines) == (5 if key == "square" else 9)**n
                assert not polygons
            if key == "square":
                close(lines[-1][1], (3**n, 0))
            if key == "fern":
                # C appears one iteration after B, which appears after A.
                assert len(polygons) == 2*(n-1)*(n-2)
                assert sum(symbol == "A" for symbol, _ in word) == 1
                assert sum(symbol == "B" for symbol, _ in word) == 2*n
            for polygon in polygons:
                assert len(polygon) == 4
                area = sum(polygon[i][0]*polygon[(i+1)%4][1]
                           - polygon[(i+1)%4][0]*polygon[i][1] for i in range(4))
                assert abs(area) > 1e-10
            for start, end, width in lines:
                assert width > 0
                assert all(math.isfinite(v) for p in (start, end) for v in p)
            obj = (ROOT/"geometry"/f"{key}-n{n:02d}.obj").read_text().splitlines()
            vertices = sum(line.startswith("v ") for line in obj)
            assert sum(line.startswith("l ") for line in obj) == len(lines)
            assert sum(line.startswith("f ") for line in obj) == len(polygons)
            for line in obj:
                if line.startswith(("l ", "f ")):
                    assert all(1 <= int(i) <= vertices for i in line.split()[1:])
            print(f"PASS {key} n={n}: {len(lines)} segments, {len(polygons)} blades")

    readme = (ROOT/"README.md").read_text()
    for target in re.findall(r"\]\(([^)]+)\)", readme):
        if not target.startswith(("http:", "https:", "#")):
            assert (ROOT/target).is_file(), target
    print("PASS README local links and OBJ vertex indices")
    print("PASS portable checks; native Houdini results are recorded in houdini/validation.json.")


if __name__ == "__main__":
    main()

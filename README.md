# Lab 05: L-System Grammars

**Yao Tang**

This lab includes solutions to the wheat and square puzzles and a custom fern grammar.

Implemented in Houdini Apprentice 22.0.466 using native L-System nodes. The rule screenshots and iteration images below come from Houdini.

## 1. Wheat grammar puzzle

| Setting | Value |
| --- | --- |
| Premise | `F` |
| Rule 1 | `F=FF[-FF]F[-FF]FF-` |
| Angle | `20` degrees |
| Step Size | `1` |
| Generations | `1`, `2`, `3` |
| Geometry Type | Skeleton |
| Random Scale | `0` |

![Wheat rules in Houdini](images/houdini/wheat-rules.png)

| n = 1 | n = 2 | n = 3 |
| --- | --- | --- |
| ![Wheat n=1](images/houdini/wheat-n01.jpg) | ![Wheat n=2](images/houdini/wheat-n02.jpg) | ![Wheat n=3](images/houdini/wheat-n03.jpg) |

Each `F` becomes five forward steps along the main path and two branches with two steps each. The branches start after the second and third steps. `[` saves the turtle state, and `]` restores it after drawing a branch.

The final `-` is outside the brackets. It turns the turtle left by 20 degrees after the last segment, so it does not change the first image. In later generations, it changes the direction of the next expanded block. This produces the bend in generation 2 and the spiral in generation 3. Removing this last turn would leave the main axis straight.

The three iterations contain 9, 81, and 729 segments. Their branch layout and turning direction match the assignment references. The images fit each iteration separately because the geometry gets larger at each step.

Rule file: [wheat.txt](grammars/wheat.txt).

## 2. Square grammar puzzle

| Setting | Value |
| --- | --- |
| Premise | `+F` |
| Rule 1 | `F=F+F-F-F+F` |
| Angle | `90` degrees |
| Step Size | `1` |
| Generations | `1`, `2`, `3` |
| Geometry Type | Skeleton |
| Random Scale | `0` |

![Square rules in Houdini](images/houdini/square-rules.png)

| n = 1 | n = 2 | n = 3 |
| --- | --- | --- |
| ![Square n=1](images/houdini/square-n01.jpg) | ![Square n=2](images/houdini/square-n02.jpg) | ![Square n=3](images/houdini/square-n03.jpg) |

The initial `+` points the turtle to the right. Each `F` becomes five segments with the turn sequence `+ - - +` between them. At generation 1, the path moves right, down, right, up, and right. It ends with the same heading it started with.

Applying the replacement to every segment creates the smaller square loops and stepped edges in generations 2 and 3. The number of segments is `5^n`, and the horizontal distance between the endpoints is `3^n` with Step Size 1. Crossings at later iterations are part of the pattern.

Rule file: [square.txt](grammars/square.txt).

## 3. Custom plant: Southern lady fern

### Reference

<img src="images/fern-reference.jpg" alt="Southern lady fern reference photograph" width="560">

Reference: [NC State Extension, Southern Lady Fern](https://plants.ces.ncsu.edu/plants/athyrium-asplenioides/). Photograph by Alan Cressler, listed as [Public Domain Mark 1.0](https://creativecommons.org/publicdomain/mark/1.0/) on that page.

I modeled one frond of this plant. The reference has a central axis with side divisions called pinnae, and each pinna has smaller divisions called pinnules. My grammar uses this hierarchy and reduces the size toward the tips. It is a flat, simplified model; the leaf edges, spores, and full clump are not modeled.

### Rules

Premise: `F(0.8,0.035)A(1)`

```text
A(s)=F(0.45*s,0.035*s)[+(68)B(0.9*s)]F(0.45*s,0.035*s)[-(68)B(0.9*s)]-(1.5)A(0.90*s)

B(s)=F(0.32*s,0.018*s)[+(55)C(0.90*s)][-(55)C(0.90*s)]F(0.28*s,0.018*s)B(0.82*s)

C(s)=[{.+(18)f(0.5*s).-(36)f(0.5*s).-(144)f(0.5*s).}][F(0.9510565*s,0.008*s)]
```

| Component | Role |
| --- | --- |
| Premise | Draws a short stalk and starts the main growing tip, `A(1)`. |
| `A(s)` | Extends the central axis and places one pinna on each side at different heights. The new tip has 90% of the previous size. A 1.5-degree turn makes the axis curve gently. |
| `B(s)` | Extends a pinna, adds a pair of pinnules, and continues with 82% of the previous size. Older pinnae have more time to grow than newly created ones. |
| `C(s)` | Draws one narrow four-vertex leaf blade and its central vein. It contains no growing symbol, so the finished blade does not subdivide again. |
| `s` | Controls the length and width of a component. `F(length,width)` sets these values explicitly. |
| `{`, `.`, `}` | Start a polygon, record its vertices, and close it. Lowercase `f` moves between vertices without drawing extra line segments. |

All turns and lengths in the fern rules are explicit. Use Step Size `1`, Random Scale `0`, and Skeleton geometry. The default Angle can remain `25`; the explicit angles override it.

### Iterations

| n = 5 | n = 8 | n = 12 |
| --- | --- | --- |
| ![Fern n=5](images/houdini/fern-n05.jpg) | ![Fern n=8](images/houdini/fern-n08.jpg) | ![Fern n=12](images/houdini/fern-n12.jpg) |

| Generation | Line segments | Leaf blades |
| --- | ---: | ---: |
| 5 | 75 | 24 |
| 8 | 213 | 84 |
| 12 | 509 | 220 |

These images use the same scale. The main axis gets longer while older side branches develop more leaves. Rule replacement is simultaneous: a `B` produced by `A` expands in the next generation, and its new `C` symbols expand one generation later. This delay leaves the newest tips less developed.

Rule file: [fern.txt](grammars/fern.txt).

## Houdini scene

Open [lab05_grammars.hipnc](lab05_grammars.hipnc) in Houdini. The `/obj/lab05_grammars` object contains nine editable L-System nodes: three wheat iterations, three square iterations, and three fern iterations. Select a node to inspect its parameters, enable its blue display flag to view it, and use the Front view. The Rules tab contains the premise and productions.

The scene stores its rules inline, so it does not need an external rule file to open. [build_lab.py](houdini/build_lab.py) rebuilds the nodes from [settings.json](grammars/settings.json) and the rule files. [capture_views.py](houdini/capture_views.py) exports the iteration images through Houdini's viewport flipbook tool. The Apprentice watermark is retained.

## Checks

All nine nodes cooked without errors or warnings in Houdini 22.0.466. Their line segments were compared with an independent 2D interpreter, including the wheat's accumulated turn and the square's endpoints. The fern outputs contain 24, 84, and 220 closed leaf polygons at generations 5, 8, and 12. The native geometry results are recorded in [validation.json](houdini/validation.json).

The `scripts/` folder contains the optional Python interpreter and preview generator. `geometry/` contains static OBJ exports from that interpreter. These support checking the grammar; the images in this report are from Houdini.

## References

- [SideFX L-System SOP documentation](https://www.sidefx.com/docs/houdini/nodes/sop/lsystem.html): turtle commands, parametric rules, and polygon syntax.
- [NC State Extension: Southern Lady Fern](https://plants.ces.ncsu.edu/plants/athyrium-asplenioides/): plant structure and reference photograph by Alan Cressler, Public Domain Mark 1.0.

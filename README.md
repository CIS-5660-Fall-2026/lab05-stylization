# lab05-grammars
Let's practice using grammars! For this lab, please pull up the L-system node in Houdini.


## 1. Wheat grammar puzzle
Look at these iterations (n = 1, 2, 3) of a one-rule grammar. Using the built in symbols in Houdini, design a grammar that produces this output. Take a screenshot of your rules.\
<img width="200" alt="square1" src="https://user-images.githubusercontent.com/1758825/193949661-a3a0e1f7-7d68-4b9e-8384-d9991e1e9fd2.png">
<img width="200" alt="square2" src="https://user-images.githubusercontent.com/1758825/193949853-cf2306b3-3537-4c24-91b5-0a3083bc87c0.png">
<img width="200" alt="square3" src="https://user-images.githubusercontent.com/1758825/193949859-5e432b4b-f18d-48b5-a9e9-8d7dba255955.png">

<img width="1897" height="1083" alt="Screenshot 2026-10-08 000357" src="https://github.com/user-attachments/assets/ae92b292-a575-4f96-b2f1-a0f917e1f584" />


## 2. Square grammar puzzle
How about this one? Take a screenshot of your rules.\
<img width="200" alt="square1" src="https://user-images.githubusercontent.com/1758825/193949895-87cdfb43-da7c-4867-ab1b-107e1ba9d2a7.png">
<img width="200" alt="square2" src="https://user-images.githubusercontent.com/1758825/193949904-a9cdfe0f-319e-4ca8-9935-dd338217a7cf.png">
<img width="200" alt="square3" src="https://user-images.githubusercontent.com/1758825/193949910-928e5993-ce26-4681-80f8-ffeb54be4dcf.png">

<img width="1487" height="1003" alt="Screenshot 2026-10-08 000458" src="https://github.com/user-attachments/assets/4c8d3eca-59fa-4df0-929b-cb2ca5218f9f" />

## 3. Custom plant
Choose a plant in the world. Working off a reference, design a grammar that mimics the structure of that plant. Unlike our simple puzzles, please use multiple rules for greater complexity. Think carefully about the structure of your grammar! EXPLAIN the structure of your plant in the README. What are the components? What do each of the rules do? Be sure to also include images of a few iterations of your output plant. 
I chose a potted palm (majesty / areca style). Its structure is a clear hierarchy:
- several stems grow out of one base in a fan
- each stem produces fronds on both sides as it grows upward
- each frond is a long central axis with leaflets in pairs on both sides
<img width="351" height="468" alt="image" src="https://github.com/user-attachments/assets/f7a41ea4-8083-42e3-869e-9db5d0fd404e" />


Rules: with angle = 20
<img width="436" height="303" alt="Screenshot 2026-10-08 000618" src="https://github.com/user-attachments/assets/615546c1-33bd-4f58-97a1-167292c3047d" />
| Symbol | Component | Role |
|---|---|---|
| `S` | Stem apex | Growing tip of a stem. Every generation it adds stem length and sprouts new fronds. |
| `A` | Frond apex | Growing tip of a frond. Every generation it extends the rachis and adds leaflets. |
| `F` | Segment | Draws a line. It has no rule, so once a segment is created it never changes. |
| `+` `-` | Turns | Rotate by the angle (20°). Doubled (`++`, `--`) for a 40° turn. |
| `[` `]` | Branching | Save the turtle state before a branch, then return to the parent axis after it. |

My thought process for rules is as below:
**Premise: `[-S][S][+S]`**
This is the clump. Three stems start from the same point at the base: one tilted 20° left, one straight up, and one tilted 20° right. Each one is wrapped in brackets so they all start at the base instead of following each other.
 
**Rule 1: `S=FF[--A][++A]S`**
This is stem growth. Each generation, every stem:
1. grows two segments upward (`FF`)
2. sprouts a pair of fronds, one 40° to the left (`[--A]`) and one 40° to the right (`[++A]`)
3. keeps its growing tip at the top (`S`), so the next generation continues from there
The result is a stem with pairs of fronds stacked along it.
 
**Rule 2: `A=F[--F][++F]A`**
This is frond growth. Each generation, every frond:
1. extends its rachis by one segment (`F`)
2. adds a pair of leaflets at 40° on either side (`[--F][++F]`)
3. keeps its growing tip at the end (`A`), so the frond keeps getting longer

Leaflets are a plain `F` with no rule, so they stay a fixed length. Only the rachis keeps growing.

n=2:
<img width="614" height="595" alt="Screenshot 2026-10-08 000654" src="https://github.com/user-attachments/assets/e1ba29e4-9e06-4311-9d5e-31355a51d5cb" />

n=4:
<img width="731" height="711" alt="Screenshot 2026-10-08 000702" src="https://github.com/user-attachments/assets/304f6854-e0ac-4e6b-8a2b-91fac07de698" />

n=6:
<img width="888" height="949" alt="Screenshot 2026-10-08 000710" src="https://github.com/user-attachments/assets/b9bf5d77-371e-4517-bba9-a6e585fb60be" />

Potential improvements:
1. Stochastic rules (e.g. two versions of Rule 1 with different frond angles, each with 50% probability) would add variation.
2. Right now the plant is planar. Maybe change the first rule so the plant can grow in 3D.

## Submission
- Create a pull request against this repository
- In your readme, list your solutions and format your README nicely
- Profit

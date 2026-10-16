# lab05-grammars
Let's practice using grammars! For this lab, please pull up the L-system node in Houdini.

## 1. Wheat grammar puzzle
Look at these iterations (n = 1, 2, 3) of a one-rule grammar. Using the built in symbols in Houdini, design a grammar that produces this output. Take a screenshot of your rules.\
![alt text](image.png)

<img width="200" alt="square1" src="https://user-images.githubusercontent.com/1758825/193949661-a3a0e1f7-7d68-4b9e-8384-d9991e1e9fd2.png">
<img width="200" alt="square2" src="https://user-images.githubusercontent.com/1758825/193949853-cf2306b3-3537-4c24-91b5-0a3083bc87c0.png">
<img width="200" alt="square3" src="https://user-images.githubusercontent.com/1758825/193949859-5e432b4b-f18d-48b5-a9e9-8d7dba255955.png">

## 2. Square grammar puzzle
How about this one? Take a screenshot of your rules.\
![alt text](image-1.png)

<img width="200" alt="square1" src="https://user-images.githubusercontent.com/1758825/193949895-87cdfb43-da7c-4867-ab1b-107e1ba9d2a7.png">
<img width="200" alt="square2" src="https://user-images.githubusercontent.com/1758825/193949904-a9cdfe0f-319e-4ca8-9935-dd338217a7cf.png">
<img width="200" alt="square3" src="https://user-images.githubusercontent.com/1758825/193949910-928e5993-ce26-4681-80f8-ffeb54be4dcf.png">

## 3. Custom plant
![alt text](image-3.png)

Choose a plant in the world. Working off a reference, design a grammar that mimics the structure of that plant. Unlike our simple puzzles, please use multiple rules for greater complexity. Think carefully about the structure of your grammar! EXPLAIN the structure of your plant in the README. What are the components? What do each of the rules do? Be sure to also include images of a few iterations of your output plant. 

### My plant: Rosemary (*Salvia rosmarinus*)

The model is a single rosemary stem: a straight main stem with pairs of narrow needle leaves pointing upward. Each leaf pair is turned 90° from the pair below it, so the leaves stick out in all directions. New leaves appear at the tip and get longer as they age, so the top of the stem tapers to a point. The L-system is drawn as green tubes (Type = Tube, followed by a Color node).

#### Components

- **Stem:** the `F` segments along the main axis.
- **Leaf pairs:** `[+L][-L]` puts one leaf on each side of the stem.
- **Roll:** `///` rolls the turtle 3 × 30° = 90° so that the next leaf pair faces a different direction.
- **Growing tip:** `A`, which adds a new node at the top every generation.

#### Grammar (Angle = 30°, Generations = 12)
![alt text](image-2.png)
Premise: `A`

| Rule | What it does |
| --- | --- |
| `A=F[+L][-L]///A` | The tip adds a stem segment and a pair of leaves, rolls 90°, then keeps growing upward. |
| `L=FM` | A new leaf grows its first segment. |
| `M=FN` | The leaf grows its second segment. |
| `N=F` | The leaf grows its third and final segment, then stops growing. |

Each leaf grows one segment per generation for three generations. As a result, the newest leaves near the tip are short and the older leaves below are full length, which gives the pointed tip.

#### Iterations

![Rosemary iterations](images/part3/rosemary_iterations.png)

Final result (n = 12):

<img width="400" alt="Rosemary L-system, n = 12" src="images/part3/rosemary_final.png">

## Submission
- Create a pull request against this repository
- In your readme, list your solutions and format your README nicely
- Profit

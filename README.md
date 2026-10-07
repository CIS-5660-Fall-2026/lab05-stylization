# Nathan Chortek Submission

## Wheat grammar puzzle

<img src="wheatRules.png">

## Square grammar puzzle

<img src="boxesRules.png">

## Custom plant

### Reference

<img src="baobabReference.png">

The tree has a very thick trunk with a relatively flat top. Each branch then grows roughly perpendicularly to from the tip of its preceding limb, with decreasing in thickness.

### Rules

<img src="baobabRules.png">

**Rule 1**
* This helps randomize the number of branches grown at each iteration. With `: 0.75`, each of the 4 possible branches in Rule 2 have a 75% chance of growing.

**Rule 2**
* `"`: Multiplies the current length by `Step Size Scale`. This causes each iteration to be shorter than the last when combined with `Step Size Scale < 1`.
* `!`: Multiplies the current thickness by `Thickness Scale`. This causes each iteration to be thinner than the last when combined with `Thickness Scale < 1`.
* `FFF`: Grows a branch forward 3 steps.
* `~(10)`: Applies a random rotational offset up to 10 degrees, adding non-uniformity to the branch directions while remaining close to a default of 90 degrees.
* `+`, `-`, `&`, `^`: Causes each of the 4 possible branches to grow perpendicularly from the tip of the preceding branch, forming a rough 4-lane "crossroads" pattern. When combined with Rule 1, each crossroad has a variable number of segments.

### Results

**5 Iterations**

<img src="baobab5.png">

**10 Iterations**

<img src="baobab10.png">

**15 Iterations**

<img src="baobab15.png">

# lab05-grammars
Let's practice using grammars! For this lab, please pull up the L-system node in Houdini.

## 1. Wheat grammar puzzle
Look at these iterations (n = 1, 2, 3) of a one-rule grammar. Using the built in symbols in Houdini, design a grammar that produces this output. Take a screenshot of your rules.\
<img width="200" alt="square1" src="https://user-images.githubusercontent.com/1758825/193949661-a3a0e1f7-7d68-4b9e-8384-d9991e1e9fd2.png">
<img width="200" alt="square2" src="https://user-images.githubusercontent.com/1758825/193949853-cf2306b3-3537-4c24-91b5-0a3083bc87c0.png">
<img width="200" alt="square3" src="https://user-images.githubusercontent.com/1758825/193949859-5e432b4b-f18d-48b5-a9e9-8d7dba255955.png">

## 2. Square grammar puzzle
How about this one? Take a screenshot of your rules.\
<img width="200" alt="square1" src="https://user-images.githubusercontent.com/1758825/193949895-87cdfb43-da7c-4867-ab1b-107e1ba9d2a7.png">
<img width="200" alt="square2" src="https://user-images.githubusercontent.com/1758825/193949904-a9cdfe0f-319e-4ca8-9935-dd338217a7cf.png">
<img width="200" alt="square3" src="https://user-images.githubusercontent.com/1758825/193949910-928e5993-ce26-4681-80f8-ffeb54be4dcf.png">

## 3. Custom plant
Choose a plant in the world. Working off a reference, design a grammar that mimics the structure of that plant. Unlike our simple puzzles, please use multiple rules for greater complexity. Think carefully about the structure of your grammar! EXPLAIN the structure of your plant in the README. What are the components? What do each of the rules do? Be sure to also include images of a few iterations of your output plant. 

## Submission
- Create a pull request against this repository
- In your readme, list your solutions and format your README nicely
- Profit

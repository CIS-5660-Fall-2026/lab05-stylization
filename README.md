# lab05-grammars

**Name:** Zhiyao Luo

## 1. Wheat Grammar

<img src="Result/result1.png" width="700">

*Wheat Grammar*
## 2. Square Grammar

<img src="Result/result2.png" width="700">

*Square Grammar*

## 3. Custom Plant

<img src="Result/reference.png" width="250">

*Reference*

<img src="Result/result3.png" width="700">

*Custom Plant*

My plant is inspired by a columnar tree with a tall central trunk and upward-growing branches.

**Premise:** `X`

**Rule 1:** `X=F[+X][-X]FX`  
**Rule 2:** `F=FF`  
**Angle:** `15`

`X` represents a growth point and `F` represents a stem.  
Rule 1 creates side branches and continues the main stem.  
Rule 2 makes the existing stems longer.

### Iterations

<img src="Result/gen3.png" width="700">

*Generation 3*

<img src="Result/gen5.png" width="700">

*Generation 5*




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

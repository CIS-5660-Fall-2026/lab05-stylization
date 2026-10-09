# lab05-grammars

![alt text](image-2.png)


Let's practice using grammars! For this lab, please pull up the L-system node in Houdini.

## 1. Wheat grammar puzzle
Look at these iterations (n = 1, 2, 3) of a one-rule grammar. Using the built in symbols in Houdini, design a grammar that produces this output. Take a screenshot of your rules.\
<img width="200" alt="square1" src="https://user-images.githubusercontent.com/1758825/193949661-a3a0e1f7-7d68-4b9e-8384-d9991e1e9fd2.png">
<img width="200" alt="square2" src="https://user-images.githubusercontent.com/1758825/193949853-cf2306b3-3537-4c24-91b5-0a3083bc87c0.png">
<img width="200" alt="square3" src="https://user-images.githubusercontent.com/1758825/193949859-5e432b4b-f18d-48b5-a9e9-8d7dba255955.png">

![alt text](image.png)

## 2. Square grammar puzzle
How about this one? Take a screenshot of your rules.\
<img width="200" alt="square1" src="https://user-images.githubusercontent.com/1758825/193949895-87cdfb43-da7c-4867-ab1b-107e1ba9d2a7.png">
<img width="200" alt="square2" src="https://user-images.githubusercontent.com/1758825/193949904-a9cdfe0f-319e-4ca8-9935-dd338217a7cf.png">
<img width="200" alt="square3" src="https://user-images.githubusercontent.com/1758825/193949910-928e5993-ce26-4681-80f8-ffeb54be4dcf.png">

![alt text](image-1.png)

## 3. Custom plant
![alt text](flower.gif)

![alt text](image-3.png)

These are the rules I used to create this flower. A is the main stem, and there are two variants for two different leaves, which are indepdently chosen with 50% probability. The (L,0,1) is a way to pass info upstream to the stamp expression in my switch statement between two leaves.

B is the formula for the flower.
C is the formula for the leaves.
D is the formula for the budding at the top (which only appears at the end since we include it after A in the Premise).

Followed this tutorial: https://www.youtube.com/watch?v=0vE8GiXhOWM


## Submission
- Create a pull request against this repository
- In your readme, list your solutions and format your README nicely
- Profit

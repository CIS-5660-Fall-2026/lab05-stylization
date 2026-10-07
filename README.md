# lab05-grammars
Let's practice using grammars! For this lab, please pull up the L-system node in Houdini.

## 1. Wheat grammar puzzle
![Puzzle1](images/puzzle1.png)
![Puzzle1 Solution](images/puzzle1-sol.png)

## 2. Square grammar puzzle
![Puzzle2](images/puzzle2.png)
![Puzzle2 Solution](images/puzzle2-sol.png)

## 3. Custom plant

This is a Japanese elm.

![Japanese Elm](images/Japanese%20Elm.png)
![Puzzle3](images/puzzle3.png)
![Puzzle Solution](images/puzzle3-sol.png)

| Iterations | Output |
|------------|--------|
| 2 | ![Iteration 1](images/puzzle3-2.png) |
| 4 | ![Iteration 2](images/puzzle3-4.png) |
| 6 | ![Iteration 3](images/puzzle3-6.png) |

Starting from Houdini L-System’s default rules, I adjusted the orientation of the branches and added more smaller branches and twigs.

**A** creates several main branches using **B** spreading in different directions.

**B** extends each main branch with FF, creates two side branches using [+F] and [-F], and then continues the recursive structure through **A**.

**C** creates four short terminal branches pointing at different angles.

## Submission
- Create a pull request against this repository
- In your readme, list your solutions and format your README nicely
- Profit

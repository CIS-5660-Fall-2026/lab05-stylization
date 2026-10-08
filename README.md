# lab05-grammars
Let's practice using grammars! For this lab, please pull up the L-system node in Houdini.
<img width="498" alt="Screenshot 2026-10-07 152437" src="https://github.com/user-attachments/assets/d0f11f8f-dcc0-4e25-9743-a9888ed124df" />
<img width="400" alt="Screenshot 2026-10-07 152426" src="https://github.com/user-attachments/assets/0cd1f151-134f-45f5-a649-c71ca1318e0e" />
<img width="400" alt="Screenshot 2026-10-07 152144" src="https://github.com/user-attachments/assets/a15643a3-7e1c-487d-b691-a56bf8133fee" />
<img width="400" alt="Screenshot 2026-10-07 152135" src="https://github.com/user-attachments/assets/780da1dd-caf4-401e-b8b9-d8f1894e6b89" />
<img width="400" alt="Screenshot 2026-10-07 152441" src="https://github.com/user-attachments/assets/2f7ea202-c121-4f2e-abca-bf6c20e51809" />

### Plant: Erdtree
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/50348d79-03e6-4971-a4ac-de4e38fe03c3" />

**Generation 12:**
<img width="1177" height="691" alt="image" src="https://github.com/user-attachments/assets/53d0140a-7aa6-41ff-8511-5b52850c212d" />
**Generation 16:**
<img width="1218" height="710" alt="image" src="https://github.com/user-attachments/assets/0e897689-8a03-4f76-88eb-dbd54d36684c" />

## Erdtree overview
The erdtree is a very tall tree with a thick root. most of its branches come out at the top of the tree, however starting 2/3rds way up there are branches that come out at sharp angles.
The branches at the top all flatten out  pretty  heavily to form the top. This aspect i didnt manage to implement, but i'm assuming if I had I would do so by taking more direct control of the angle via parameters, like i did with the `B(i)`
## Rules:
Premise: `F(15)~(c)F~(c)F~(c)B(4)E`

Rules:
```
B(i)="(1.2)[A][$A]~(2)F(i)B(0.8*i)
A=!(0.3)F[^^~(30)C]//[^^~(30)C]//[^^~(30)C]
C=!"FF~(10)T[D]C
D=!(0.5)"(0.5)~(60)C : 0.3
```
The premise starts the bottom of the trunk that has no branches off it, and makes it slightly not straight.
B: Trunk of the tree
A: Point from which branches come out of
C: Branch
D: Optional split in a branch
### Rule explanation in depth:
The base shrinks via the parameter i, but I also do `"(1.2)` so the branches get longer the higher they are on the tree. `[$A]` happened to flip the branch positions around, i'm not sure why it works better than `|` or `/(180)`.

The rest is pretty self explanitory, I randomly extend three branches from each point A, Im always shrinking the thickness and slightly the lengths as I go.

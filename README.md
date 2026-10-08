# Lab 05 – L-System Grammars

Made with the L-System SOP in Houdini 21.0.

## 1. Wheat Grammar Puzzle

- Premise: `F`
- Rule: `F=FF[+FF]F[+FF]FF+`
- Angle: `20`

The trailing `+` isn't visible at n = 1. From n = 2 on, every rewritten segment ends with a turn, so the stem curls.

| n = 1 | n = 2 | n = 3 |
|:---:|:---:|:---:|
| <img src="img/1_1.png" width="260"> | <img src="img/1_2.png" width="260"> | <img src="img/1_3.png" width="260"> |

## 2. Square Grammar Puzzle

- Premise: `+F`
- Rule: `F=F+F-F-F+F`
- Angle: `90`

Each segment is replaced by a square notch.

| n = 1 | n = 2 | n = 3 |
|:---:|:---:|:---:|
| <img src="img/2_1.png" width="260"> | <img src="img/2_2.png" width="260"> | <img src="img/2_3.png" width="260"> |

## 3. Custom Plant – Cherry Blossom Tree

<img src="img/ref.png" width="450">

*Reference: "Yoshino cherry ソメイヨシノ" by SLIMHANNYA, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Yoshino_cherry_ソメイヨシノ.jpg), CC BY-SA 4.0.*

A cherry tree has a short trunk that splits into about three limbs. The limbs keep forking into a wide, slightly drooping crown, with clusters of flowers along the twigs.

```
Premise: FA
A=[&B]////[&B]////[&B]
B=!"TF[+B]///[-B]F[C]J
C=[&FJ][^FJ]
```
Angle `35`, Step Size Scale `0.75`, Gravity `0.2`. `J` copies a small pink sphere.

| Rule | Component | What it does |
|---|---|---|
| `FA` | Trunk | One trunk segment, then the fork `A` |
| `A` | Fork | Splits into 3 limbs spaced evenly around the trunk |
| `B` | Branch | Gets thinner and shorter, droops a little (`T`), and forks into two `B`s in different planes. Adds a flower cluster `C` along the branch and a blossom `J` at the end |
| `C` | Flower cluster | Two short stalks, each with a blossom |

<img src="img/rules.png" width="49%"> <img src="img/values.png" width="49%">

| n = 2 | n = 3 | n = 4 |
|:---:|:---:|:---:|
| <img src="img/3_2.png" width="260"> | <img src="img/3_3.png" width="260"> | <img src="img/3_4.png" width="260"> |

| n = 5 | n = 6 |
|:---:|:---:|
| <img src="img/3_5.png" width="390"> | <img src="img/3_6.png" width="390"> |

# COMP 163 - Project 2: Text Adventure

**Chapters 3 and 4: Types and Branching**

Write a Python program that runs a short choose-your-own-adventure story. The
player types their choice, the story branches on what they typed, and different
paths lead to different endings.

> **If anything here disagrees with the instructions on Canvas, Canvas is
> correct.** This file exists so the exact required output sits next to your
> code. Canvas has the full assignment description, the grading breakdown, the
> due date, and any updates posted after the project was released.

The setting, the characters and the plot are entirely yours. The structure
below is not.

Your file is `adventure.py`.

## What your program does

The player makes three choices in a row. The words they type are fixed, so the
autograder knows what to send:

| Choice | The player types |
|---|---|
| First | `left` or `right` |
| Second | `fight` or `run` |
| Third | `take` or `leave` |

Use `input()` for each one and compare with `==`.

**The two graded paths below must ask for exactly these three inputs and no
more.** This one is quiet and expensive, so read it twice.

The autograder sends three answers and then stops. A fourth `input()` anywhere
along a graded path waits for a fourth answer that never arrives, and your
program dies right there, before it prints an ending. Nothing on screen tells
you that happened. It costs 13 of the 40 points on code that otherwise works.

On any other path, add as many extra decision points as you like, using any
words you like. It is only the two graded paths that are fixed at three.

## The two graded paths

Two specific runs are graded, so their outcomes are fixed:

- `left`, then `fight`, then `take` **must end in a win**
- `right`, then `run`, then `leave` **must end in a loss**

Every other combination is yours to decide. A path may end early, and not every
path has to reach a third choice.

## Required output

Four things must appear exactly as written. Everything else on screen is your
story, in your words.

**The health line.** Your player starts with 10 health.

Print it on its own line **before you ask for the first choice**, so the first
health line every run prints is exactly:

```
Health: 10
```

That line has to appear even on a run where the very first answer is invalid,
which is why it goes before you read any input at all. Print it after the first
`input()` instead and you lose both bad-answer tests, 11 points, on a program
that is otherwise fine.

After that, print the current value again after each choice. The number has to
actually change as the story goes on. Print it as a whole number.

**The two endings.** A win prints this line:

```
=== YOU WIN ===
```

A loss prints this line:

```
=== GAME OVER ===
```

Copy both exactly, including the spaces and all three equals signs on each
side. A run that reaches one ending must not also print the other.

Print each ending with `print()`, so the marker finishes the line it is on.
Putting it inside an `input()` prompt does not count, because that leaves the
rest of your output stuck to the end of it.

**Bad input.** If the player types something that is not one of the valid words
for that choice, print this and stop:

```
Invalid choice.
```

This applies to **every** choice, not just the first one. A bad answer to the
second or third question has to stop the game the same way.

Two rules follow from that, and both are graded:

- A run that prints `Invalid choice.` must not reach either ending.
- A run that reaches an ending must not print `Invalid choice.` anywhere.

## What your program must contain

Three things are required, and they are checked by reading your code, not your
output:

1. **At least one `elif`.**
2. **At least one compound condition** joined by `and` or `or`.
3. **At least one numeric comparison** using `<`, `<=`, `>` or `>=`. Comparing
   the choice words with `==` does not count. This is about the health value.

## What you may use

**This project covers Chapters 3 and 4. Material from Chapter 5 and above is
not allowed.**

You may use anything from Chapters 1 through 4:

- everything Project 1 used: variables, `input()`, arithmetic, `float()`,
  `int()`, `str()`, `print()`
- comparisons (`==`, `!=`, `<`, `<=`, `>`, `>=`)
- boolean operators (`and`, `or`, `not`)
- `if`, `elif`, `else`

Nothing from Chapter 5 onward, which rules out:

| Not allowed here | Chapter |
|---|---|
| `for` and `while` loops | 5 |
| String methods such as `.lower()`, `.strip()`, `.upper()` | 6 |
| Functions you define yourself (`def`) | 7 |
| Opening or reading files | 8 |
| Classes | 9 |
| `try` / `except` | 11 |
| `import` of anything | 12 |

Because there is no `.lower()`, your comparisons are case sensitive exactly as
you write them. Pick whether your valid words are lowercase, uppercase or
capitalised, stay consistent, and make the prompt tell the player what to type.

The autograder checks this on every push, and the check is worth 4 points, so
reaching ahead costs you those 4 straight away. That is not the whole cost. A
confirmed use of a later chapter is a zero on the project once I review it. The
4 points are the early warning, not the penalty.

## Check your work before you push

```
python3 check.py
```

This runs every check the autograder runs, except the commit count, and tells
you which requirement any failure came from. If `check.py` is clean, the
autograder will be too.

## Grading (40 points)

| Component | Points |
|---|---|
| File header filled in | 3 |
| At least 3 commits | 2 |
| Concept check (required and forbidden features) | 4 |
| Win path reaches the win ending | 7 |
| Health tracked correctly on the win path | 6 |
| Loss path reaches the loss ending | 7 |
| A bad **first** answer stops the game | 5 |
| A bad **second** answer stops the game | 6 |
| **Total** | **40** |

### About the header

The first lines of `adventure.py` must be filled in:

```
# Name: Your Name
# Date: 2026-10-02
# Description: A short description of your adventure
```

The file ships with those labels blank. Blank scores nothing.

### About the commits

You get 2 points for making at least three commits. This is not busywork and it
is not about the number.

A commit is a save point you can come back to. When you break something at 11pm,
the ability to return to the last version that worked is the difference between
a small problem and starting over. Commits are also the record of how the work
actually happened, which matters when you are asked to show your process, and it
is how you would hand work to someone else on a team.

Commit when you finish a piece, not all at once at the end:

```
git add adventure.py
git commit -m "First choice branches on left and right"
git push
```

Three is the floor, not the goal.

## Submitting

Two steps, and you need both:

1. **Push to this repository.** Every push runs the checks automatically, and
   the most recent push before the deadline is what gets graded.
2. **Paste this repository's URL into the Canvas assignment.**

The URL by itself grades nothing. It tells me which repository is yours. It
looks something like:

```
https://github.com/COMP-163/fall-2026-comp163-project-2-yourusername
```

Copy it out of your browser's address bar rather than typing it. Push early and
push often.

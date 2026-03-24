# Stage Two — What's on the card?

## Description

In Stage 1, we learnt how to create a dynamic flashcard from user's input. Let's add a primitive guessing mechanism as well so that the user can check how well they remember the definitions.

For this stage you'll extend the flashcard-creation mechanism implemented in Stage 1 and add a functionality to check the user's answer on top of it.

---

## Objectives

Similar to Stage 1, your program should read two lines from the console, a **term**, and a **definition**, that represent a card. However there's no need to print `Card:` or `Definition:` in this stage.

After that, the user inputs a line as an answer (a definition of the term on the card). Compare the user's answer with the correct definition and print the result.

The output of the program must be one of the following:

* `Your answer is wrong...` if the answer doesn't match the definition;
* `Your answer is right!` if the answer matches the definition.

Of course, at this point, the user is unlikely to get the answer wrong, since they're the ones who just typed in the answer... But don't worry: right now we're just warming up so that in later stages we could make this a bit more challenging for our users.

---

## Examples

The greater-than symbol followed by a space (`> `) represents the user input. Note that it's not part of the input.

**Example 1: the user's answer is correct**

Input (a term, a definition, an answer):

```no-highlight
> print()
> outputs text
> outputs text
```

Output:

```no-highlight
Your answer is right!
```

**Example 2: the user's answer is incorrect**

Input (a term, a definition, an answer):

```no-highlight
> Jetbrains
> A place for people who love to code
> A place for people who hate to code
```

Output:

```no-highlight
Your answer is wrong...
```

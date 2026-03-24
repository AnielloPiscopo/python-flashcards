# Make it your own

## Description

Your program can only entertain users with one card, which isn't really fun. Let's take our game to the next level and implement a set of flashcards.

Let the user decide how many cards they would like to make. First, ask the player to enter the desired number of cards. Then, ask them to input the term and the definition for every flashcard.

In the end, once all flashcards have been defined and saved, your program is finally ready to be used as a game! Question the player about all the new words they have entered. The program should give the term and ask for its definition.

---

## Objectives

Your program should do the following:

* Get the number of flashcards the user would like to create. To do that, print the line `Input the number of cards:` as a prompt for the user, and then read the number from the next line.
* Create the defined amount of cards in a loop. To create a flashcard, print the line `The term for card #n:` where n is the index number of the card to be created; then read the user's input (the term) from the following line. Then print the line `The definition for card #n:` and read the user's definition of the term from the next line. Repeat until all the flashcards are created.
* Test the user on their knowledge of the definitions of all terms in the order they were added. To do that with one flashcard, print the line `Print the definition of "term":` where `"term"` is the term of the flashcard to be checked, and then read the user's answer from the following line. Make sure to put the term of the flashcard in quotes. Then print the line `Correct!` if the user's answer is correct, or the line `Wrong. The right answer is "definition".` if the answer is incorrect, where `"definition"` is the correct definition. Repeat for all the flashcards in the set.

---

## Example

The symbol `> ` represents the user input. Note that it's not part of the input.

```no-highlight
Input the number of cards:
> 2
The term for card #1:
> print()
The definition for card #1:
> outputs text
The term for card #2:
> str()
The definition for card #2:
> converts to a string
Print the definition of "print()":
> outputs text
Correct!
Print the definition of "str()":
> outputs text
Wrong. The right answer is "converts to a string".
```

> Note that all your outputs and user inputs should be on separate lines.

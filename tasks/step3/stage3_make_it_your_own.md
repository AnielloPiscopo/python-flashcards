# Stage Three — Make it your own

## Description

Your program can only entertain users with one card, which isn't really fun. Let's take our game to the next level and implement a set of flashcards.

Let the user decide how many cards they would like to make. First, ask the player to enter the desired number of cards. Then, ask them to input the term and the definition for every flashcard.

In the end, once all flashcards have been defined and saved, your program is finally ready to be used as a game! Question the player about all the new words they have entered. The program should give the term and ask for its definition.

---

## Objectives

1. Stampa `Input the number of cards:` e leggi il numero di carte
2. Per ogni carta (da 1 a n), in un loop:
   - Stampa `The term for card #n:` e leggi il termine
   - Stampa `The definition for card #n:` e leggi la definizione
3. Testa l'utente su tutte le carte nell'ordine in cui sono state inserite:
   - Stampa `Print the definition of "term":` e leggi la risposta
   - Se corretta → stampa `Correct!`
   - Se errata → stampa `Wrong. The right answer is "definition".`

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

> ⚠️ Note: all your outputs and user inputs should be on separate lines.

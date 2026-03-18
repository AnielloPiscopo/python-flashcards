# Stage Four — A good stack

## Description

While learning new things, we may mix things up and use the right definition for the wrong term. Let's inform our players if they enter the definition that is wrong for the requested flashcard but correct for another flashcard in our set.

Also, it might be very confusing if our flashcard set contains cards with the same term or definition. Let's add a constraint: the user must add only unique terms and definitions.

---

## Objectives

1. Leggi il numero di carte
2. Per ogni carta, in un loop:
   - Chiedi il termine. Se esiste già → stampa `The term "term" already exists. Try again:` e richiedi finché non è unico
   - Chiedi la definizione. Se esiste già → stampa `The definition "definition" already exists. Try again:` e richiedi finché non è unica
3. Testa l'utente su tutte le carte:
   - Se la risposta è corretta → `Correct!`
   - Se la risposta è sbagliata ma è la definizione corretta di un altro termine → `Wrong. The right answer is "correct answer", but your definition is correct for "term for user's answer".`
   - Se la risposta è semplicemente sbagliata → `Wrong. The right answer is "definition".`

---

## Examples

The symbol `> ` represents the user input. Note that it's not part of the input.

**Example 1: the user tries to add duplicated term and definition**

```no-highlight
Input the number of cards:
> 2
The term for card #1:
> print()
The definition for card #1:
> outputs text
The term for card #2:
> print()
The term "print()" already exists. Try again:
> str()
The definition for card #2:
> outputs text
The definition "outputs text" already exists. Try again:
> converts to a string
Print the definition of "print()":
> outputs text
Correct!
Print the definition of "str()":
> converts to a string
Correct!
```

**Example 2: the user gives a correct definition for a term that exists, but which is not the term that the program is asking about**

```no-highlight
Input the number of cards:
> 2
The term for card #1:
> uncle
The definition for card #1:
> a brother of one's parent
The term for card #2:
> ankle
The definition for card #2:
> a part of the body where the foot and the leg meet
Print the definition of "uncle":
> a part of the body where the foot and the leg meet
Wrong. The right answer is "a brother of one's parent", but your definition is correct for "ankle".
Print the definition of "ankle":
> ???
Wrong. The right answer is "a part of the body where the foot and the leg meet".
```

> ⚠️ Note: all your outputs and user inputs should be on separate lines.

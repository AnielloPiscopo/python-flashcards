# Menu, please!

## Description

Our users cannot create new flashcards all the time. It seems like a good idea to keep old but useful cards in storage so we can use them later. Let's try to do that!

In this stage, you will improve the application's interactivity by having it ask the user for action and perform it. You will also provide additional functionality, allowing the user to store flashcards in files for future use.

The program should support the following actions:

* add a card: `add`
* remove a card: `remove`
* load cards from file: `import`
* save cards to file: `export`
* ask for definitions of some random cards: `ask`
* exit the program: `exit`

You can store cards in a file in any format; tests do not check the content of the file, but they do check that the saved flashcards are loaded correctly.

When you load flashcards from a file, you shouldn't erase the cards that aren't in the file. If the imported flashcard already exists, update its definition in the program memory. There won't be any conflict with definitions in the tests.

---

## Objectives

Print the message `Input the action (add, remove, import, export, ask, exit):` each time the user is prompted for their next action. The action is read from the next line, processed, and the message is output again until the user decides to exit the program.

The program's behavior depends on the action the user inputs:

* `add` — create a new flashcard with a unique term and definition. After adding the card, output the message `The pair ("term":"definition") has been added`, where `"term"` is the term entered by the user and `"definition"` is the definition entered by the user. If a term or a definition already exists, output the line `The <term/definition> already exists. Try again:` and accept a new term or definition.
* `remove` — ask the user for the term of the card they want to remove with the message `Which card?`, and read the user's input from the next line. If a matching flashcard exists, remove it from the set and output the message `The card has been removed.`. If there is no such flashcard in the set, output the message `Can't remove "card": there is no such card.`, where `"card"` is the user's input.
* `import` — print the line `File name:`, read the user's input from the next line, which is the file name, and import all the flashcards written to this file. If there is no file with such name, print the message `File not found.`. After importing the cards, print the message `n cards have been loaded.`, where n is the number of cards in the file. The imported cards should be added to the ones that already exist in the memory of the program. However, the imported cards have priority: if you import a card with the name that already exists in the memory, the card from the file should overwrite the one in memory.
* `export` — request the file name with the line `File name:` and write all currently available flashcards into this file. Print the message `n cards have been saved.`, where n is the number of cards exported to the file.
* `ask` — ask the user about the number of cards they want and then prompt them for definitions, like in the previous stage.
* `exit` — print `Bye bye!` and finish the program.

---

## Examples

The symbol `> ` represents the user input. Note that it's not part of the input.

**Example 1: the user removes an existing card and tries to remove a non-existent one.**

```no-highlight
Input the action (add, remove, import, export, ask, exit):
> add
The card:
> France
The definition of the card:
> Paris
The pair ("France":"Paris") has been added.

Input the action (add, remove, import, export, ask, exit):
> add
The card:
> France
The card "France" already exists. Try again:
> Great Britain
The definition of the card:
> Paris
The definition "Paris" already exists. Try again:
> London
The pair ("Great Britain":"London") has been added.

Input the action (add, remove, import, export, ask, exit):
> remove
Which card?
> France
The card has been removed.

Input the action (add, remove, import, export, ask, exit):
> remove
Which card?
> Wakanda
Can't remove "Wakanda": there is no such card.

Input the action (add, remove, import, export, ask, exit):
> exit
Bye bye!
```

**Example 2: the user uses files to import and export their flashcards; definitions of existing cards are updated after import**

```no-highlight
Input the action (add, remove, import, export, ask, exit):
> import
File name:
> ghost_file.txt
File not found.

Input the action (add, remove, import, export, ask, exit):
> add
The card:
> Japan
The definition of the card:
> Tokyo
The pair ("Japan":"Tokyo") has been added.

Input the action (add, remove, import, export, ask, exit):
> add
The card:
> Russia
The definition of the card:
> UpdateMeFromFile
The pair ("Russia":"UpdateMeFromFile") has been added.

Input the action (add, remove, import, export, ask, exit):
> import
File name:
> capitals.txt
28 cards have been loaded.

Input the action (add, remove, import, export, ask, exit):
> ask
How many times to ask?
> 1
Print the definition of "Russia":
> Moscow
Correct!

Input the action (add, remove, import, export, ask, exit):
> export
File name:
> capitalsNew.txt
29 cards have been saved.

Input the action (add, remove, import, export, ask, exit):
> exit
Bye bye!
```

**Example 3: the program asks for definitions several times**

```no-highlight
Input the action (add, remove, import, export, ask, exit):
> add
The card
> a brother of one's parent
The definition of the card
> uncle
The pair ("a brother of one's parent":"uncle") has been added.

Input the action (add, remove, import, export, ask, exit):
> add
The card
> a part of the body where the foot and the leg meet
The definition of the card
> ankle
The pair ("a part of the body where the foot and the leg meet":"ankle") has been added.

Input the action (add, remove, import, export, ask, exit):
> ask
How many times to ask?
> 6
Print the definition of "a brother of one's parent":
> ankle
Wrong. The right answer is "uncle", but your definition is correct for "a part of the body where the foot and the leg meet".
Print the definition of "a part of the body where the foot and the leg meet":
> ??
Wrong. The right answer is "ankle".
Print the definition of "a brother of one's parent":
> uncle
Correct!
Print the definition of "a part of the body where the foot and the leg meet":
> ankle
Correct!
Print the definition of "a brother of one's parent":
> ??
Wrong. The right answer is "uncle".
Print the definition of "a part of the body where the foot and the leg meet":
> uncle
Wrong. The right answer is "ankle", but your definition is correct for "a brother of one's parent".

Input the action (add, remove, import, export, ask, exit):
> exit
Bye bye!
```

> ⚠️ Note that all your outputs and user inputs should be on separate lines.

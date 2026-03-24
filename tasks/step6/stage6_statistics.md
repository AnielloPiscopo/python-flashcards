# Statistics

## Description

While studying, it may be very helpful to pay more attention to challenging parts where you make the most mistakes. In this stage, you will add some statistics features to your program so that the users can track their progress.

Implement the following additional actions:

* save the application log to the given file: `log`
* print the term or terms that the user makes most mistakes with: `hardest card`
* erase the mistake count for all cards: `reset stats`

Remember that now you need to store three items (term, definition, mistakes) instead of two (term, definition).

You may want to take a look at `io.StringIO` objects: handling the log will be easier with them.

---

## Objectives

Print the message `Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):` each time the user is prompted for their next action. The action is read from the next line, processed, and the message is output again until the user decides to exit the program.

The program's behavior depends on the user's input action:

* `log` — ask the user where to save the log with the message `File name:`, save all the lines that have been input in/output to the console to the file, and print the message `The log has been saved.` Don't clear the log after saving it to the file.
* `hardest card` — print a string that contains the term of the card with the highest number of wrong answers, for example, `The hardest card is "term". You have N errors answering it`. If there are several cards with the highest number of wrong answers, print all of the terms: `The hardest cards are "term_1", "term_2"`. If there are no cards with errors in the user's answers, print the message `There are no cards with errors.`
* `reset stats` — set the count of mistakes to 0 for all the cards and output the message `Card statistics have been reset.`

Update your `import` and `export` actions from the previous stage, so that the error count for each flashcard is also imported and exported.

---

## Example

The symbol `> ` represents the user input. Note that it's not part of the input.

```no-highlight
Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> hardest card
There are no cards with errors.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> import
File name:
> capitals.txt
28 cards have been loaded.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> hardest card
The hardest card is "France". You have 10 errors answering it.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> ask
How many times to ask?
> 1
Print the definition of "Russia":
> Paris
Wrong. The right answer is "Moscow", but your definition is correct for "France" card.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> hardest card
The hardest cards are "Russia", "France". You have 10 errors answering them.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> reset stats
Card statistics have been reset.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> hardest card
There are no cards with errors.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> log
File name:
> todayLog.txt
The log has been saved.

Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
> exit
Bye bye!
```

> ⚠️ Note that all your outputs and user inputs should be on separate lines.

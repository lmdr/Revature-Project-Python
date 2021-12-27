# Revature Python Project: Guess My Number Game

A command line interface application implementing the "Guess My Number" game. The player selects the range of numbers a random integer will be generated by inputting a minimum and maximum number. A pseudo-random number is generated in that range and the player must guess the number by inputting their guess in the command line.

### Technology Stack

This project makes use of the following technologies:

Technology | Version
---------- | -------
Python | 3.9.9
VS Code | 1.63.2

### Libraries

This project makes use of the following libraries:

- logging
- random
- unittest

### How to Run

Install the technologies above and clone the repository.

From VS Code (or a terminal) run the project.

Initially the user will see the following:

```
Negative inputs will exit.
Enter a minimum number: 
```

Enter a negative number to exit the application or enter a minimum number for the range:

```
Enter a minimum number: 0
Enter a maximum number: 
```

Enter a negative number to exit the application or enter a maximum number for the range:

```
Enter a maximum number: 100
Enter your guess: 
```

Enter your guess for the random number:

```
Enter your guess: 0
```

After making your guess, you will see one of three messages:

```
You guessed the number!
Your guess is less than the number.
Your guess is greater than the number.
```

If you guessed the number, congratulations!

Else, adjust your guess and try again until you guess the correct number.

```
Enter your new guess: 248
Your guess is greater than the number.
Enter your new guess: 244
Your guess is less than the number.
```

When you finish a game (when you have guessed the correct number), the following message will be displayed:

```
You guessed the number!
It took 1 guess to guess 0.
```

You may choose to play again by choosing the range for the random number to be generated in, or you may exit by entering a negative number.

```
Negative inputs will exit.
Enter a minimum number: -4
Exiting...
```

### Sample Usage

This section shows a sample on how the program might be used.

```
Negative inputs will exit.
Enter a minimum number: 0
Enter a maximum number: 5 
Enter your guess: 0
Your guess is less than the number.
Enter your new guess: 1
Your guess is less than the number.
Enter your new guess: 2
Your guess is less than the number.
Enter your new guess: 3
You guessed the number!
It took 4 guesses to guess 3.
Negative inputs will exit.
Enter a minimum number: 0
Enter a maximum number: 10
Enter your guess: 5
Your guess is less than the number.
Enter your new guess: 6
Your guess is less than the number.
Enter your new guess: 7
You guessed the number!
It took 3 guesses to guess 7.
Negative inputs will exit.
Enter a minimum number: -1
Exiting...
```

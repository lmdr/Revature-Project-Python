"""logging for log messages,
   random for generating a number to guess,
   sys for exit()"""
import logging
import random
import sys



class Guess:
    """Guess My Number game implementation"""

    def check_guess(self, number, player_guess):
        """Test the player's guess against the pseudo-randomly generated number"""
        if number is player_guess:
            logging.info("CHECK GUESS %i == %i", number, player_guess)
            print("You guessed the number!")
            return True
        elif number < player_guess:
            logging.info("CHECK GUESS %i < %i", number, player_guess)
            print("Your guess is greater than the number.")
        else:
            logging.info("CHECK GUESS %i > %i", number, player_guess)
            print("Your guess is less than the number.")
        return False

    def main(self):
        """Guess My Number game logic/flow"""
        # Keep going until user enters negative number
        while True:
        # Generate random integer
            print("Negative inputs will exit.")
            # Get minimum number for random integer range
            minimum = int(input("Enter a minimum number: "))
            if minimum < 0:
                logging.warning("EXITING...")
                sys.exit()
            # Get maximum number for random integer range
            maximum = int(input("Enter a maximum number: "))
            while maximum < 0 or maximum < minimum:
                if maximum < 0:
                    logging.warning("EXITING...")
                    sys.exit()
                else:
                    logging.warning("MAXIMUM < MINIMUM.")
                    maximum = int(input("Enter a new maximum number: "))
            number = random.randint(minimum, maximum)

            # Get guesses from user
            guess = int(input("Enter your guess: "))
            count_guesses = 1
            # Continue until player guesses correct number
            while not Guess.check_guess(self, number, guess):
                guess = int(input("Enter your new guess: "))
                count_guesses += 1

            logging.info("GUESS SUCCESS NUMBER %i GUESSES %i", number, count_guesses)
            if count_guesses == 1:
                print(f"It took {count_guesses} guess to guess {number}.")
            else:
                print(f"It took {count_guesses} guesses to guess {number}.")



if __name__ == '__main__':
    Guess.main(Guess)

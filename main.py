import logging, random

class Guess:
  def check_guess(number, player_guess):
    if number is player_guess:
      logging.info(f"CHECK GUESS {number} == {player_guess}")
      print("You guessed the number!")
      return True
    elif number < player_guess:
      logging.info(f"CHECK GUESS {number} < {player_guess}")
      print("Your guess is greater than the number.")
    else:
      logging.info(f"CHECK GUESS {number} > {player_guess}")
      print("Your guess is less than the number.")
    return False

  def main():
    # Keep going until user enters negative number
    while True:
      # Generate random integer
      print("Negative inputs will exit.")
      # Get minimum number for random integer range
      min = int(input("Enter a minimum number: "))
      if min < 0:
        logging.warning("EXITING...")
        exit()
      # Get maximum number for random integer range
      max = int(input("Enter a maximum number: "))
      while max < 0 or max < min:
        if max < 0:
          logging.warning("EXITING...")
          exit()
        else:
          logging.warning("MAXIMUM < MINIMUM.")
          max = int(input("Enter a new maximum number: "))
      number = random.randint(min, max)
      
      # Get guesses from user
      guess = int(input("Enter your guess: "))
      count_guesses = 1
      # Continue until player guesses correct number
      while not Guess.check_guess(number, guess):
        guess = int(input("Enter your new guess: "))
        count_guesses += 1
      

      logging.info(f"GUESS SUCCESS NUMBER {number} GUESSES {count_guesses}")
      if count_guesses == 1:
        print(f"It took {count_guesses} guess to guess {number}.")
      else:
        print(f"It took {count_guesses} guesses to guess {number}.")

if __name__ == '__main__':
  Guess.main()

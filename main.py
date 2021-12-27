import logging, random, unittest

class Guess:
  def check_guess(number, player_guess):
    if number is player_guess:
      print("You guessed the number!")
      return True
    elif number < player_guess:
      print("Your guess is greater than the number.")
    else:
      print("Your guess is less than the number.")
    return False

  def main():
    while True:
      print("Negative inputs will exit.")
      min = int(input("Enter a minimum number: "))
      if min < 0:
        print("Exiting...")
        exit()
      max = int(input("Enter a maximum number: "))
      while max < 0 or max < min:
        if max < 0:
          print("Exiting...")
          exit()
        else:
          print("Maximum is less than minimum.")
          max = int(input("Enter a new maximum number: "))
      number = random.randint(min, max)
      guess = int(input("Enter your guess: "))
      count_guesses = 1
      while not Guess.check_guess(number, guess):
        guess = int(input("Enter your new guess: "))
        count_guesses += 1
      if count_guesses == 1:
        print(f"It took {count_guesses} guess to guess {number}.")
      else:
        print(f"It took {count_guesses} guess(es) to guess {number}.")

if __name__ == '__main__':
  Guess.main()
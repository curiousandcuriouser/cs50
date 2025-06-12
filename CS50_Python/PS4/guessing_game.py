import random
import sys

def main():
  level = get_level()
  random_number(level)

# Prompts the user for a level, 
  
def get_level():
  while True:
    try: 
        level = int(input("Level: "))

        # Reprompt if not positive integer
        if level < 1:
          continue

        else:
          return level
    except ValueError:
      sys.exit

def random_number(level):
  number = random.randint(1, level)

  while True:
    try: 
        guess = int(input("Guess: "))
        
        # Reprompt if not positive integer
        if guess < 1:
          continue
        else:
          break
    except ValueError:
      sys.exit

  if guess == number:
    print("Just right!")
  elif guess > number:
    print("Too large!")
  else:
    print("Just right!")

main()

# Randomly generates an integer between 1 and, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.
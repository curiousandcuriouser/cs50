import random

def main():
  level = get_level()
  random_number(level)

# Prompts the user for a level, 
  
def get_level():
  while True:
    level = input("Level: ")

    # Reprompt if not positive integer
    if level < 1:
      continue
    else:
      return level

def random_number():
  number = random.

# Randomly generates an integer between 1 and, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.
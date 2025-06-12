import random
import sys

def main():
  level = get_level()
  generate_integer(level)
  get_answers()
  display_score()


# Prompts the user for a level
  # If the user does not input 1, 2, or 3, the program should prompt again.
def get_level():
  while True:
    try: 
        level = int(input("Level: "))

        # Reprompt if not positive integer
        if level < 0 or level > 3:
          continue

        else:
          return level
    except ValueError:
      sys.exit()

# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with n digits. No need to support operations other than addition (+).
def generate_integer(level):
  if level == 1:
    int1 = random.randint(0, 9)
    int2 = random.randint(0, 9)
  elif level == 2:
    int1 = random.randint(0, 99)
    int2 = random.randint(0, 99)
  else:
    int1 = random.randint(0, 999)
    int2 = random.randint(0, 999)

  score = 0
  attempt = 0
  repetition = 0

  while repetition < 11:
    answer = input(f"{int1} + {int2} = ")
    sum = int1 + int2
    print(sum)

    while attempt < 4:
      if answer == sum:
        score += 1
      elif answer != sum:
        attempt += 1
        print("EEE")
    print(score)

#Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
def get_answers():
    ...

# The program should ultimately output the user’s score: the number of correct answers out of 10.
def display_score():
    ...

if __name__ == "__main__":
    main()
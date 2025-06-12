import random
import sys

def main():
  level = get_level()
  generate_integer(level)


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
  score = 0
  repetition = 0

  while repetition < 10:
    if level == 1:
      int1 = random.randint(0, 9)
      int2 = random.randint(0, 9)
    elif level == 2:
      int1 = random.randint(0, 99)
      int2 = random.randint(0, 99)
    else:
      int1 = random.randint(0, 999)
      int2 = random.randint(0, 999)
    
    attempt = 0
    correct_sum = int1 + int2 # works

    while attempt < 3:
      while True:
        try:
          answer = int(input(f"{int1} + {int2} = "))
          break
        except ValueError:
          attempt += 1
          print("EEE")
          continue

      if answer == correct_sum:
        score += 1
        repetition += 1
        break
      elif answer != correct_sum:
        attempt += 1
        print("EEE")
        if attempt == 3:
          repetition += 1
          break

  print(f"Score: {score}")

if __name__ == "__main__":
    main()
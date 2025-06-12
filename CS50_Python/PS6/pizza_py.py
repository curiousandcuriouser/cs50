from tabulate import tabulate
import sys

# If the user does not specify exactly one command-line argument, or file not ending .py, or file not exist, exit via sys.exit.
try:
  if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit()
  elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()
  elif not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit()

  with open(sys.argv[1]) as file:
    lines = file.readlines()

except FileNotFoundError:
    print("File does not exist")
    sys.exit()

# Output a table formatted as ASCII art using tabulate
print()

import sys

# If the user does not specify exactly one command-line argument, or file not ending .py, or file not exist, exit via sys.exit.
try:
  if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit()
  elif len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit()
  elif not sys.argv[1].endswith(".py"):
    print("Not a Python file")
    sys.exit()

  with open(sys.argv[1]) as file:
    lines = file.readlines()

except FileNotFoundError:
    print("File does not exist")
    sys.exit()

count = 0

for line in lines:
  if line.startswith("#"):
    pass
  elif line.isspace():
    pass
  else:
    count += 1

#Outputs the number of lines of code in that file, excluding comments and blank lines
print(count)

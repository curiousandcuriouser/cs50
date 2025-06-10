# Prompts the user for names, one per line, until the user inputs control-d
def main ():
  names = get_names()
  adieu(names)

def get_names():
  names = []
  while True:
    try:
      # Ask for input and convert to UPPERCASE
      name = input("Name: ").title()
      names.append(name)
        
    # Stop when use input Ctrl + D
    except EOFError:
      print()
      return names


def adieu(names):
  if len(names) == 1:
    print(f"Adieu, adieu, to {names[0]}.")
  elif len(names) == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}.")
  else:
    print("Adieu, adieu, to ", end="")
    i = len(names)
    j = 0
    while i > 1:
      print(f"{names[j]}, ", end="")
      i -= 1
      j += 1
    if i == 1:
      print(f"and {names[j]}.")
      i -= 1

main()
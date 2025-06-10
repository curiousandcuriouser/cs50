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
  count = len(names)

  if count == 1:
    print(f"Adieu, adieu, to {names[0]}.")
  elif count == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}.")
  else:
    initial_names = ", ".join(names[:-1])
    print(f"Adieu, adieu, to {initial_names}, and {names[-1]}.")

main()
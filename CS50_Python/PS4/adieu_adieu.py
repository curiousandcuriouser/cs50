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

main()
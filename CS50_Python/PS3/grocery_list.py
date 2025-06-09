def main():
  get_item()
  display_list()


def get_item():
  shopping_list = []

  # Prompt  user for items, one per line
  while True:
    try:
      # Ask for input and convert to UPPERCASE
      item = input("Item: ").upper()
      shopping_list.append(item)
      print(f"{shopping_list}")
    

        
    # Stop when use input Ctrl + D
    except EOFError:
      return shopping_list


def display_list():
# Output the user’s grocery list
  # in all uppercase
  # sorted alphabetically
  # prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
  sorted(shopping_list)

main()
shopping_list = []

# Prompt  user for items, one per line
while True:
  try:
    # Ask for input and convert to UPPERCASE
    item = input("Item: ").upper()
    shopping_list.append(item)
      
  # Stop when use input Ctrl + D
  except EOFError:
    print("\n")
    break
  else:
    pass

# Output the user’s grocery list
  # in all uppercase
  # sorted alphabetically
  # prefixing each line with the number of times the user inputted that item. No need to pluralize the items. 
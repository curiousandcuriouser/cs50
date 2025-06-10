def main():
  shopping_list = get_item()
  display_list(shopping_list)

# Prompt  user for items
def get_item():
  shopping_list = []
  while True:
    try:
      # Ask for input and convert to UPPERCASE
      item = input("Item: ").upper()
      shopping_list.append(item)
        
    # Stop when use input Ctrl + D
    except EOFError:
      return shopping_list


# Output the user’s sorted grocery list with count
def display_list(shopping_list):
  from collections import Counter
  item_count = Counter(shopping_list)
  print("Shopping List:")
  for item, item_count in sorted(item_count.items()):
    print(f"{item_count} {item}")

main()
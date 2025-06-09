menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
  try:
    # Ask for input and convert to Title Case
    item = input("Item: ").title()

    # Find item prace and add to total
    if item in menu:
      price = menu[item]
      total += price
      print(f"${total:.2f}")
      
  # Stop when use input Ctrl + D
  except EOFError:
    print("\n")
    break
  else:
    pass
  





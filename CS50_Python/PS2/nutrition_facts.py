# Make dict for fruit info
fruits = {
  "apple": "130",
  "avocado": "50",
  "banana": "110",
  "cantaloupe": "50",
  "grapefruit": "60",
  "grapes": "90",
  "honeydew melon": "50",
  "kiwi": "90",
  "lemon": "15",
  "lime": "20",
  "nectarine": "60",
  "orange": "80",
  "peach": "60",
  "pear": "100",
  "pineapple": "50",
  "plums": "70",
  "strawberries": "50",
  "cherries": "100",
  "tangerine": "50",
  "watermelon": "80",
}


while True:
  # Prompt user for fruit input
  fruit = input("Fruit: ").lower()
  
  # Output calories for one portion
  if fruit in fruits:
    calories = fruits[fruit]
    print(f"Calories: {calories}")
    break
  else:
    print("Try a different fruit!")

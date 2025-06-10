from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
font = figlet.getFonts()


# Prompts the user for a str of text
text = input("What text do you want to modify? ")

if len(sys.argv) == 1 or len(sys.argv) == 3:
  # Set random font
  if len(sys.argv) == 1:
    random_font = random.choice(figlet.getFonts())
    figlet.setFont(font=random_font)
  # Sets desired font
  elif len(sys.argv) == 3:
    desired_font = sys.argv[2]
    if desired_font not in figlet.getFonts():
      print("Invalid font")
      print("Available fonts: acrobatic, alligator, bubble, caligraphy, coinstak, diamond, eftiwater, fuzzy, isometric3, pawp, roman, speed, ticks, weird. Add -f font to program")
      sys.exit()
    else:
      figlet.setFont(font=desired_font)

# Expects zero or two command-line arguments  
else:
  print("Please provide 0 or two arguments!")

# Output modified text
print(figlet.renderText(text))
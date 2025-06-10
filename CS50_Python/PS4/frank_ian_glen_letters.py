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
  if len(sys.argv) == 3:
    figlet.setFont(sys.argv[2])

# Expects zero or two command-line arguments  
else:
  print("Please provide 0 or two arguments!")

# Output modified text
print(figlet.renderText(text))
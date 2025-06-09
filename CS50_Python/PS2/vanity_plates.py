# Start with 2 letters <
# Max. 6 char or int <
# Min. 2 char or int <
# No int in middle of plate, only at the end
# First number != 0
# No period, spaces, or punctuation <

# Validate if input is valid

def main():
  plate = input("Plate: ")

  if is_valid(plate):
    print("Valid")
  else:
      print("Invalid")

character_list = []
print(f"{character_list}")

def is_valid(plate):
  for character in plate:
      character_list.append(character)
      print(f"{character_list}")
  
  if 2 > len(character_list) > 6:
    print("Failed at: 2 > len(character_list) > 6")
    return False

  for character in character_list:
    if character.isalpha() or character.isdigit():
      pass
    else:
      print("Failed at: all numbers & letters")
      break
    
    if character == character_list[0] or character == character_list[1] and character.isalpha():
      pass
    else:
      print("Failed at: first 2 digits")
      break

main()
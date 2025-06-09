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

def is_valid(plate):
  if 2 > len(plate) > 6:
    print("Failed at: 2 > len(character_list) > 6")
    return False
  
  if not plate[0].isalpha() or not plate[1].isalpha():
    print("Failed at: first 2 digits")
    return False

  for character in plate:
    if character.isalpha() or character.isdigit():
      pass
    else:
      print("Failed at: all numbers & letters")
      break

    
    
    for i in range(len(plate)):
      if character.isalpha() and plate[i + 1].isdigit() and plate[i + 2].isalpha():
        break

main()
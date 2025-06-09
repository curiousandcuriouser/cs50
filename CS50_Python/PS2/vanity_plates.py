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
  if 2 > len(plate) or len(plate) > 6:
    print("Failed at: 2 > len(character_list) > 6")
    return False
  
  if not plate[0].isalpha() or not plate[1].isalpha():
    print("Failed at: first 2 digits")
    return False

  in_number = False
  
  for i in range(len(plate)):
    character = plate[i]
    if not character.isalnum():
      print("Failed at: all numbers & letters")
      return False
  
    if character.isdigit():
      if not in_number:
        if character == '0':
          print("Failed at: first number is 0")
          return False
        in_number = True
    elif character.isalpha():
      if in_number:
        print("Failed at: letter after a number (number in middle)")
        return False
  return True

main()
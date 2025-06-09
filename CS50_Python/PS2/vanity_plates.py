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
  # Validate plate char length
  if 2 > len(plate) or len(plate) > 6:
    return False
  
  # Validate first 2 characters letters
  if not plate[0].isalpha() or not plate[1].isalpha():
    return False

  in_number = False
  
  
  for i in range(len(plate)):
    character = plate[i]

    # Validate all plate char digits and letters
    if not character.isalnum():
      return False
  

    if character.isdigit():
      # Check if first number is 0
      if not in_number:
        if character == '0':
          return False
        in_number = True

    # Check if letter after number
    elif character.isalpha():
      if in_number:
        return False
  # If not false, then valid
  return True

main()
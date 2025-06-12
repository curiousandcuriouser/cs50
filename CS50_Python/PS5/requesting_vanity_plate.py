def main():
  plate = input("Plate: ")
  print(is_valid(plate))

def is_valid(plate):
  # Validate plate char length
  if 2 > len(plate) or len(plate) > 6:
    return f"Invalid"
  
  # Validate first 2 characters letters
  if not plate[0].isalpha() or not plate[1].isalpha():
    return f"Invalid"

  in_number = False
  
  for i in range(len(plate)):
    character = plate[i]

    # Validate all plate char digits and letters
    if not character.isalnum():
      return f"Invalid"
  
    if character.isdigit():
      # Check if first number is 0
      if not in_number:
        if character == '0':
          return f"Invalid"
        in_number = True

    # Check if letter after number
    elif character.isalpha():
      if in_number:
        return f"Invalid"
  # If not false, then valid
  return f"Valid"

if __name__ == "__main__":
  main()
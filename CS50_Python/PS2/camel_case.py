camel_case = input("camelCase: ")
camel_case = camel_case.strip()


# Split on upper case
snake_case_list = []

for character in camel_case:
  if character.isupper():
    snake_case_list.append("_") # If character is uppercase, add _
    snake_case_list.append(character.lower()) # Then add character in lowercase
  else: 
    snake_case_list.append(character) # Otherwise add character as is

snake_case = "".join(snake_case_list) # Join the list together

print(f"snake_case: {snake_case}")
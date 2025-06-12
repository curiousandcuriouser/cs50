def main():
  message = input("Input: ")
  print(shorten(message))

def shorten(message):
  vowels = ['A', 'E', 'I' ,'O', 'U', 'a', 'e', 'i', 'o', 'u']

  message_list = []

  for character in message:
    if character in vowels:
      pass
    else:
      message_list.append(character)

  output = "".join(message_list) # Join the list together
  return f"Output: {output}"

if __name__ == "__main__":
  main()
def convert(str):
  return str.replace(":)", "🙂").replace(":(", "🙁")

userInput = input("Add the emoji you want to convert: ")
emojiInput = convert(userInput)
print(f"{emojiInput}")

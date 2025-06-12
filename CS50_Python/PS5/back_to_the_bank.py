def main():
  greeting = input()
  print(value(greeting))

def value(greeting):
  greeting = greeting.strip().lower()

  if greeting == "hello":
    return f"$0"
  elif greeting[0] == "h":
    return f"$20"
  else: 
    return f"$100"

if __name__ == "__main__":
  main()
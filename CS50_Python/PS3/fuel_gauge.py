def main():
  x = display_fuel("Provide a fraction in this format, X / Y: ")
  print(x)

def display_fuel(prompt):
  # Prompt for input: X/Y
  while True:
    try:
      x, y = input(prompt).split("/")
      if x > y:
        continue
      percentage = round((int(x) / int(y))*100)

      # Display take gauge:
      if 1 < percentage < 99:
        return f"{percentage}%"
      elif percentage <= 1:
        return "E"
      else:
        return "F"

    except (ValueError, ZeroDivisionError):
      return

main()







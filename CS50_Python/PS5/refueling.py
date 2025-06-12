def main():
  percentage = convert(input("Provide a fraction in this format, X / Y: "))
  print(gauge(percentage))

def convert(fraction):
  # Prompt for input: X/Y
  while True:
    try:
      x, y = input(fraction).split("/")
      if x > y:
        continue
      percentage = round((int(x) / int(y))*100)
      return percentage
    except (ValueError, ZeroDivisionError):
      return

def gauge(percentage):
    # Display take gauge:
    if 1 < percentage < 99:
      return f"{percentage}%"
    elif percentage <= 1:
      return "E"
    else:
      return "F"

if __name__ == "__main":
  main()
def main():
  fraction = input("Provide a fraction in this format, X / Y: ")
  percentage = convert(fraction)
  print(gauge((percentage)))

def convert(fraction):
  # Prompt for input: X / Y
  while True:
    try:
      x, y = fraction.split("/")
      if x > y:
        continue
      percentage = round((int(x) / int(y))*100)
      return int(percentage)
    except (ValueError, ZeroDivisionError):
      return

def gauge(percentage):
    # Display take gauge:
    if 1 < int(percentage) < 99:
      return f"{percentage}%"
    elif int(percentage) <= 1:
      return "E"
    else:
      return "F"

if __name__ == "__main":
  main()
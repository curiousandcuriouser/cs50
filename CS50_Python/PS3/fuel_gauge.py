# Prompt for input: X/Y
while True:
  try:
    fraction = input("Provide a fraction in this format, X / Y: ")
    break
  except (ValueError, ZeroDivisionError):
    pass

# Split numbers and calculate fraction
numbers = fraction.split("/")
calculate = int(numbers[0]) / int(numbers[1])

# Convert to percentage & round
percentage = round(calculate * 100)

# Display take gauge:
if 1 < percentage < 99:
  print(f"{percentage}%")
elif percentage <= 1:
  print("E")
else:
  print("F")





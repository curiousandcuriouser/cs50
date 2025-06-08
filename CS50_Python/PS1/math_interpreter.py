variables = input("Give me one integer, one operator, and another integer: ")

arguments = variables.split()
operator = arguments[1]

if operator == "+":
  answer = float(arguments[0]) + float(arguments[2])
elif operator == "-":
  answer = float(arguments[0]) - float(arguments[2])
elif operator == "*":
  answer = float(arguments[0]) * float(arguments[2])
elif operator == "/":
  answer = float(arguments[0]) / float(arguments[2])
else:
  print("INVALID!")

print(f"{answer:.1f}")

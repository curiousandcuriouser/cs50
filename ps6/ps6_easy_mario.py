height = int(input("How high should the pyramid be? "))


i = 1
while i <= height:
  print(" " * (height - i) + "#" * i)
  i += 1

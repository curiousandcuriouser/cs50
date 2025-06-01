height = input("How high should the pyramid be? ")

try: 
  height = int(height)
except ValueError: 
  height = input("How high should the pyramid be? ")

while height < 1 or height > 8:
  height = int(input("How high should the pyramid be? ")) 

i = 1
while i <= height:
  print(" " * (height - i) + "#" * i)
  i += 1

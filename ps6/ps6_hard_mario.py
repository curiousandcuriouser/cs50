while True:
  height = input("How high should the pyramid be?  ")
  
  try: 
    height = int(height)
    
    if height > 0 and height < 9:
      break
  except ValueError:
    pass


i = 1
while i <= height:
  print(" " * (height - i) + "#" * i + " " + "#" * i)
  i += 1

def main():
  time = input("What time it is? ")
  time = convert(time)

  if 7.0 <= time <= 8.0:
    print("breakfast time")
  elif 12.0 <= time <= 13.0:
    print("breakfast time")
  elif 18.0 <= time <= 19.0:
    print("dinner time")
  else:
    return

def convert(time):
  hour = float(time.split(":")[0])
  minutes = (float(time.split(":")[1])) * float(1/60)
  time = float(hour + minutes)
  return time

main()   
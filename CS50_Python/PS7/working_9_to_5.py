import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
  if match := re.search(r"(1[0-2]|0?[0-9]:?[0-5][0-9] (?:AM|PM)) to (1[0-2]|0?[0-9]:?[0-5][0-9] (?:AM|PM))", s):
  
    first = time(match.group(1))
    last = time(match.group(2))
    
    converted_time = first + " to " + last
    return converted_time

  else:
    return "ValueError"
      

def time(group):
  if "PM" and ":" in group:
    hour, minute = group.removesuffix("PM").split(":")
    hour = int(hour) + 12
    group = str(hour) + ":" + minute
    return group
  
  elif "PM" in group:
    hour = group.removesuffix("PM")
    hour = int(hour) + 12
    group = str(hour) + ":00"
    return group
  
  elif "AM" and ":" in group:
    group = group.removesuffix("AM")
    return group
    
  elif "AM" in group:
    group = group.removesuffix("AM") + ":00"
    return group 

if __name__ == "__main__":
    main()
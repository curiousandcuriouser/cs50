import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
  if match := re.search(r"([0-1][0-9]:?[0-1][0-2][AM|PM]) to ([0-1][0-2]:?[0-1][0-9][AM|PM])"):
    first = match.group(1)
    second = match.group(2)

    converted_first = first

    if "PM" and ":" in first:
      hour, minute = first.removesuffix("PM").split(":")
      hour = hour + 12
      first = hour + ":" + minute
      return first
    
    elif "PM" in first:
      hour, minute = first.removesuffix("PM")
      hour = hour + 12
      first = hour
      return first
    
    elif "AM" and ":" in first:
      first = first.removesuffix("AM")
      return first
      
    else:
      first = first.removesuffix("AM") + ":00"
      return first

  converted_time = converted_first + "to" + converted_second
  return 
    


# For AM and PM: 
# Pattern: [0-1][0-9]:?[0-1][0-2][AM | PM]to[0-1][0-2]:?[0-1][0-9][AM | PM]

# For 
"""
from PS7.working_9_to_5 import convert



def test_conversion():
  assert "9 AM to 5 PM" == "09:00 to 17:00"
  assert "9:00 AM to 5:00 PM" == "09:00 to 17:00"
  assert "10 AM to 8:50 PM" == "10:00 to 20:50"
  assert "10:30 PM to 8 AM" == "22:30 to 08:00"

def test_error():
  assert "9:60 AM to 5:60 PM" == ValueError
  assert "9 AM - 5 PM" == ValueError
  assert "09:00 AM - 17:00 PM" == ValueError
"""

...


if __name__ == "__main__":
    main()
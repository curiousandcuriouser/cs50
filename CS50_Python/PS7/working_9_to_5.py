import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
  if match := re.search(r"(1[0-2]|0?[0-9]):?[0-5][0-9] (?:AM|PM) to (1[0-2]|0?[0-9]):?[0-5][0-9] (?:AM|PM)", s):
    return f"MATCH: {match}"

    """
    first = match.group(1)
    second = match.group(2)

    converted_first = first
    for _ in match.group():
      if "PM" and ":" in match.group(_):
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
    """
  else:
    return ValueError
      

"""
# For AM and PM: 
# Pattern: [0-1][0-9]:?[0-1][0-2][AM | PM]to[0-1][0-2]:?[0-1][0-9][AM | PM]

# For 
"""

if __name__ == "__main__":
    main()
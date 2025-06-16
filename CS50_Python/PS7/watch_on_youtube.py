import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
  if match := re.search(r"src=[\"'](https?:\/\/(?:www\.)?youtube\.com\/embed\/[^\"']+)[\"']", s):
    full_link = match.group(1)
    formatted_link = full_link.replace("www.youtube.com/embed", "youtu.be")
    return formatted_link

  
  else:
    return f"None"
    # Find the correct section
    # Strip all befre " and after "
    # Remove embed
    # Make youtube to youtu.be
    # Remove www.

if __name__ == "__main__":
    main()
import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
  if re.search("youtube", s):
    return True
  else:
    return f"None"
    # Find the correct section
    # Strip all befre " and after "
    # Remove embed
    # Make youtube to youtu.be
    # Remove www.

if __name__ == "__main__":
    main()
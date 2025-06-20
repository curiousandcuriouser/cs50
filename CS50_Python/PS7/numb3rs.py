import re
import sys

def main():
  print(validate(input("IPv4 Address: ")))

def validate(ip):
  range = r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])"
  pattern = rf"^{range}\.{range}\.{range}\.{range}$"
  if re.search(pattern, ip):
    return True
  else:
    return False

if __name__ == "__main__":
  main()
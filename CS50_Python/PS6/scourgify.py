import csv
import sys

try:
  if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit()
  elif len(sys.argv) > 4:
    print("Too many command-line arguments")
    sys.exit()
  elif not sys.argv[1].endswith(".csv"):
    print("Not a CSV file")
    sys.exit()

  students = []

  with open(sys.argv[1], "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        full_name, house = row[0], row[1]
        cleaned_full_name = full_name.strip('"')
        last, first = cleaned_full_name.split(",", 1) 
        students.append({"first": first.strip(), "last".strip(): last, "house": house.strip()})
  
  with open(sys.argv[2], "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
    writer.writeheader() 
    writer.writerows(students)

except FileNotFoundError:
    print("File does not exist")
    sys.exit()
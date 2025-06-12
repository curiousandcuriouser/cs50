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

  with open(sys.argv[1]) as infile:
    for student in infile:
        full_name, house = student[0], student[1]

        cleaned_full_name = full_name.strip('"')
        last, first = student.split(",", 1)
        student = {"first": first, "last": last, "house": house}
        students.append(student)
  
  with open("after.csv", "w") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
    writer.writerow({"first": first, "last": last, "house": house})

except FileNotFoundError:
    print("File does not exist")
    sys.exit()
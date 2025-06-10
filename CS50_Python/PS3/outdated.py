months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main ():
  date = get_date()
  convert_date(date)

def get_date():
  while True:
    date = input("Date in month-day-year format: ")
    date.split("/")
    date.split(" ", ",")

    if not date[0] in months:
      continue
    if not 0 < date[1] < 13:
      continue
    if not date[3] > 0:
      continue
    else: 
      return date

def convert_date():
  print("\n")

main()





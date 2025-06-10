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

    if "/" in date:
      date = date.split("/")
      if not 0 < int(date[0]) < 13:
        print("Error months num")
        continue

    elif "," in date:
      date = date.replace(",", "")
      date = date.split(" ")
      if not date[0] in months:
        print("Error months word")
        continue
    else:
      print("Split Issue")
      return
    
    
    if not int(date[2]) >= 0:
      print("Error year")
      continue
    elif not 0 < int(date[1]) < 32:
      print("Error day")
      continue
    else: 
      return date

def convert_date(date):
  day = int(date[1])
  year = date[2]
  month = date[0]

  if month.isalpha():
    # Find if  month is in list, convert, and print
    if month in months:
      month = months[month]
      print(f"{day:02}/{month:02}/{year}")
  elif month.isdigit():
    print(f"{day:02}/{month:02}/{year}")

main()





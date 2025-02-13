import datetime
date_input = input("Enter date (mm/dd/yyyy): ")
month, day, year = map(int, date_input.split('/'))
date = datetime.datetime(year, month, day)
print(date.strftime("%B %d, %Y"))
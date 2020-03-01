import datetime
from datetime import date
import calendar
date = input()
month, day , year = (int(i) for i in date.split(" "))
d = datetime.date(year, month, day)
print(d.strftime("%A"))

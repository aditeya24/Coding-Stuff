#Program 3: using datetime
from datetime import datetime
import calendar
dt = datetime.today() #Create object with current date and time
print(dt.strftime("%d/%m/%Y")) #Output current date 
print(dt.strftime("%B %d, %Y")) #Output current date with month name
print(dt.strftime("%X")) #Output current time
cal = calendar.TextCalendar() 
cal.prmonth(dt.year, dt.month) #Output calendar of current month

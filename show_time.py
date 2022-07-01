import time
from datetime import date
from datetime import datetime
Time=time.localtime()
current=time.strftime("%H:%M:%S", Time)
print("The current time is: ", current)
Date = date.today()
print("Today's date:", Date)
print("The current day is: ",datetime.today().strftime('%A'))


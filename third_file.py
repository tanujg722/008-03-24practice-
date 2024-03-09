#How to write current date and time in python.

import datetime

now = datetime.datetime.now()
print("Current date and time is: ")
print(now,strftime("%y-%m-%d %H:%M:%S"))

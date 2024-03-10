#How to write current date and time in python.

import datetime

now = datetime.datetime.now()
print("Current date and time is: ")
print(now,strftime("%y-%m-%d %H:%M:%S"))


# How to find area of a circle in python.
from math import pi
r = float(input("write the radius of the ciorcle: "))
print("the arae of the circle is: " str(r) + "is: " + str(pi * r**2))
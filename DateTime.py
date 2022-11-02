#Print Date and Time in python.


import datetime

now = datetime.datetime.now()
print("Date and Time now: ")
print(now.strftime("%Y-%m-%d %H-%M-%S"))

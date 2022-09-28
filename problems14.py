# Date and time with local standard


import time
tim = time.localtime();

print(time.strftime("%a %b %d %Y %H:%M:%S %Z", tim))
#Write a program to display a month of a year given by user..

import calendar

yy = int(input("Enter the year: "));
mm = int(input("Enter the month: ")); 
dd = 9                                  # Also can print without dd
print(calendar.month(yy, mm, dd));

days = int(input("How many days this year? "))

year = 365
leapYear = 366
dayHours = 24
hourMin = 60
minSec = 60

sum1 = year * dayHours * hourMin * minSec 
sum2 = leapYear * dayHours * hourMin * minSec

if days == year:
  print("The number of seconds in this year is", sum1)
else:
  print("The number of secondsin this year is", sum2)

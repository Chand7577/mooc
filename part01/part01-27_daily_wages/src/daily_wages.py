# Write your solution here
"""Hourly wage: 8.5
Hours worked: 3
Day of the week: Monday
Daily wages: 25.5 euros"""

HourlyWage=float(input('Hourly wage:'))
Hours=int(input("Hours worked:"))
Day=(input("Day of the week:"))

dailyWages=0

if Day!='Sunday':
    dailyWages=Hours*HourlyWage

else:
    dailyWages=Hours*(HourlyWage*2)

print("Daily wages:",dailyWages,"euros")
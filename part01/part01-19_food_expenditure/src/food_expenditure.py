# Write your solution hereHow many times a week do you eat at the student cafeteria? 4
"""How many times a week do you eat at the student cafeteria? 4
The price of a typical student lunch? 2.5
How much money do you spend on groceries in a week? 28.5

Average food expenditure:
Daily: 5.5 euros
Weekly: 38.5 euros"""



numDays=int(input('How many times a week do you eat at the student cafeteria?'))
lunchPrice=float(input("The price of a typical student lunch?"))
groceryCostWeek=float(input('How much money do you spend on groceries in a week?'))

weekly=(groceryCostWeek+(numDays*lunchPrice))
daily=weekly/7

print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")
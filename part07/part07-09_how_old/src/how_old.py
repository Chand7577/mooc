# Write your solution here
from datetime import datetime


def check_year(year:int):
    return True if year<2000 else False



day=int(input("Day:"))
month=int(input("Month:"))
year=int(input("Year:"))
user_dob=datetime(year,month,day)

eve_millennium=datetime(1999,12,31)


if check_year(year):
    print(f"You were {(eve_millennium-user_dob).days} days old on the eve of the new millennium.")

else:
    print(f"You weren't born yet on the eve of the new millennium.")

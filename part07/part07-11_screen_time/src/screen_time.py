import os
from datetime import datetime, timedelta

def format_date(date_):
    return datetime.strftime(date_, "%d.%m.%Y")



def store(filename: str, mins: dict, start_date, end_date):
    total = 0
    for key, value in mins.items():
        for item in mins[key]:
            total += int(item)

 
  
    with open(filename,"w") as file:
        # if mode=='w':
        file.write(f"Time period: {start_date}-{end_date}\n")
        file.write(f"Total minutes: {total}\n")
        file.write(f"Average minutes: {total/len(mins)}\n")

        
        for key, value in mins.items():
            mins_list = "/".join(mins[key])
            file.write(f"{key}: {mins_list}\n")

screen_time_data={}

filename = input('Filename:')
start_date = input("Starting date:")

# Format the start date
start_date = datetime.strptime(start_date, "%d.%m.%Y").date()

days = int(input("How many days:"))
print("Please type in screen time in minutes on each day (TV computer mobile):")

# Calculate the end date
end_date = (start_date + timedelta(days=days - 1))
end_date = format_date(end_date)

for day in range(days):
    calculated_date = start_date + timedelta(days=day)
    calculated_date = format_date(calculated_date)

    screen_time = input(f'Screen time {calculated_date}: ')
    key = f"{calculated_date}"
    screen_time_data[key] = screen_time.split()

# Store the data
store(filename, screen_time_data, format_date(start_date), end_date)

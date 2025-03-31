# Write your solution here

num=int(input("Please type in a num:"))

total_combinations=num**2



for left_val in range(1,num+1):
    for value in range(1,num+1):
        print(f"{left_val} x {value} = {left_val*value}")
        

# Write your solution here


num=int(input("Please type in a number"))
magnitudes=[1000,100,10]

for value in range(len(magnitudes)):
    if num<magnitudes[value]:
        print(f"This number is smaller than {magnitudes[value]}")
    
    else:
        continue

print("Thank you!")
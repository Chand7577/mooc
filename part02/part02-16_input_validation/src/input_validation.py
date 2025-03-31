from math import sqrt
# Write your solution here


num=int(input("Please type in a number:"))

while True:

    if num==0:
        print("Exiting...")
        break

    elif num<0:
        print("Invalid number")

    else:
        print(sqrt(num))

    num=int(input("Please type in a number:"))

 
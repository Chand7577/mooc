# Write your solution here


string=input("Please type in a string")


stars=20-len(string)


if len(string)<20:
    print("*"*stars+string)
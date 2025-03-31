# Write your solution here


string1=input("Please type in string1:")
string2=input("Please type in string2:")

if len(string1)==len(string2):
    print("The strings are equally long")

elif len(string1)>len(string2):
    print(f"{string1} is longer")

else:
    print(f"{string2} is longer")
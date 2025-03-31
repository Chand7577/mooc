# Write your solution here

"""Sample output
Person 1:
Name: Alan
Age: 26
Person 2:
Name: Ada
Age: 27
The elder is Ada"""



print("Person1:")
name1=input("Name:")
age1=int(input("Age:"))
print("Person 2:")
name2=input("Name:")
age2=int(input("Age:"))

if age1>age2:
    print("The elder is ",name1)

elif age2>age1:
    print("The elder is ",name2)

else:
    print(f"{name1} and {name2} are of the same age")
 

# Write your solution here









num1=int(input("Number1:"))
num2=int(input("Number2:"))
operation=input("Operation:")
operator=""

if operation=="add":
    result=num1+num2
    operator="+"


elif operation=="subtract":
    result=num1-num2
    operator="-"

elif operation=="multiply":
    result=num1*num2
    operator="*"


if operation in ["add","subtract","multiply"]:

    print(f"{num1} {operator} {num2} = {result}")

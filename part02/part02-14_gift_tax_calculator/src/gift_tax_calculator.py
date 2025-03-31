# Write your solution here

value_gift=int(input("Value of gift:"))

tax=0
message=""
if value_gift<5000:
    message="No tax!"


elif  value_gift>5000 and value_gift<25000:
    tax=100+(value_gift-5000)*0.08


elif value_gift>25000 and value_gift<55000:
    tax=1700+(value_gift-25000)*0.1


elif value_gift>55000 and value_gift<200000:
    tax=4700+(value_gift-55000)*0.12


elif value_gift>200000 and value_gift<1000000:
    tax=22100+(value_gift-200000)*0.15


else:
    tax=142100+(value_gift-1000000)*0.17


if tax!=0:
    print(f"Amount of tax: {tax} euros")

else:
    print(message)


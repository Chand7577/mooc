# Write your solution here

temp_F=int(input("Please type in a temperature (F):"))

temp_C=(temp_F-32)*(5/9)

if temp_C<0:
    print(f"{temp_F} degrees Fahrenheit equals {temp_C} degrees Celsius")
    print("Brr! It's cold in here!")

else:
    print(f"{temp_F} degrees Fahrenheit equals {temp_C} degrees Celsius")

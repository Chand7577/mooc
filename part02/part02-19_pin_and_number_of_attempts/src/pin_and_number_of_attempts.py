# Write your solution here

attempts=1
pin=4321
pin_number=int(input("PIN:"))

while pin_number!=pin:
    
    attempts+=1
    
    print("Wrong")
    pin_number=int(input("PIN:"))


if attempts==1:
    print(f"Correct! It only took you one single attempt!")

else:
    print(f"Correct! It took you {attempts} attempts")


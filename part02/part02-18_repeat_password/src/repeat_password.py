# Write your solution here



password=input("Password:")
repeatPassword=input("Repeat password")

while password!=repeatPassword:
    print("They do not match!")    
    repeatPassword=input("Repeat password")


print("User account created!")
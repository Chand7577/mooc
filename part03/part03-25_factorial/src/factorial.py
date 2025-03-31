# Write your solution here

num=int(input('Please type in a numbers:'))


while num>0:
    fac=1
    for value in range(1,num+1):
        fac=fac*value

    print(f"The factorial of the number {num} is {fac}")


    num=int(input('Please type in a numbers:'))

print("Thanks and bye!")
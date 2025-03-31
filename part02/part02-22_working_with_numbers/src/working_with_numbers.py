# Write your solution here


print("Please type in integer numbers. Type in 0 to finish.")
num=int(input("Number:"))



posNums=0
negNums=0
nums=[]
while num!=0:
    if num>0:
        posNums+=1
    
    elif num<0:
        negNums+=1
    
    
    nums.append(num)
    num=int(input("Number:"))


print(f"Numbers typed in {len(nums)}")
print(f"The sum of the numbers is {sum(nums)}")
print(f"The mean of the numbers is {sum(nums)/len(nums)} ")
print(f"Positive numbers {posNums}")
print(f"Negative numbers {negNums}")
# Write your solution here

num=int(input("Upper limit:"))
base=int(input("Base:"))


power=1

current=1
while current<=num:
    print(current)      # 1                 #4 power=2
    current=base**power    #8   
    power+=1
    
   
# Write your solution here

# Write your solution here

string=input("Please type in a string:")

for row in range(len(string)):
    if row==0:
        print(string[len(string)-1],end="")  
    
    
    else:
        row=len(string)-row-1
        for col in range(row,len(string)):
            
            print(string[col],end="")

    print()        


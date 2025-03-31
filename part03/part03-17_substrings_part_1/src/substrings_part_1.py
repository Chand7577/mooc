# Write your solution here

string=input("Please type in a string:")

for row in range(len(string)):
    if row==0:
        print(string[0],end="")  
       
    
    else:
        
        for col in range(row+1):
            print(string[col],end="")

    print()        


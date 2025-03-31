# Write your solution here

string=input("Word:")

spaces=30-len(string)-2


if spaces%2!=0:
    left_space=spaces//2
    right_space=spaces-left_space
   
else:
    left_space=spaces//2
    right_space=spaces//2

left_space_count=0

string_count=0

for row in range(3):
    for col in range(30):
        
        if row==1 and (col==0 or col==29):
            print("*",end="")

        
       
        elif row==1 and (col>0 or col<29):
            if left_space_count<left_space:
                print(" ",end="")
                left_space_count+=1
                
            elif string_count<len(string):
               
                print(string[string_count],end="")
                string_count+=1
            else:
                print(" ",end="")
                

        else:
            print("*",end="")


    print()
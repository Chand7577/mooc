# Write your solution here


string=input("Please type in a word:")
subString=input("Please type in a substring:")


start_value=string.find(subString)+len(subString)
index=string.find(subString,start_value)
if index!=-1:
    print(f"The second occurrence of the substring is at index {index}.")

else:
    print(f"The substring does not occur twice in the string.")

    
  
        

    
   
 
# Write your solution here

string=input("Please type in a word:")
char=input("Please type in a char:")

index_of_char=string.find(char)

count=0

if index_of_char==len(string)-1:
    pass

elif index_of_char==-1:
    pass

else:
    chars=string[index_of_char:]
    while count<3 and len(chars)>2:
        
        
        print(string[index_of_char],end="")
        
        count+=1
        index_of_char+=1



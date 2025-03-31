# Write your solution here








def squared(string, integer):
    total = 0
    text = (string*(integer*integer))
    while total < integer*integer:
        print(text[total:total+integer])
        total +=integer
    




# below is my solution 
# def squared(string,num):
#     for i in range(num):
#         for j in range(num):
#             print(nextChar(string),end="")

#         print()
           
# def nextChar(string):
#     global pos
#     pos+=1
#     if len(string)==pos:
#         pos=0
#     return string[pos]       



if __name__=="__main__":
    pos=-1
    squared("ab",2)
    # squared("aybabtu", 5)
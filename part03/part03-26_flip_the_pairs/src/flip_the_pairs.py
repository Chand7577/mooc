# Write your solution here

num=int(input("Please type in a number:"))

"""
   5  6  7  8  10
1  2  2  2  2  2
2  1  1  1  1  1
3  4  4  4  4  4
4  3  3  3  3  3
5  5  6  6  6  6
6     5  5  5  5
         7  7  8
            6  7
               10
                9 


"""    

numbers=[value for value in range(1,num+1)]


if len(numbers)==2:
    numbers[0]+=1
    numbers[1]-=1


else:
    for current in range(0,len(numbers)-2+1,2):
        if numbers[current]<numbers[current+1]:
            numbers[current]+=1
            numbers[current+1]-=1
        


for value in numbers:
    print(value)

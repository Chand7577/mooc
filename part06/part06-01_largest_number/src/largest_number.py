# write your solution here

def largest():
    numbers=[]
    with open('numbers.txt') as file:
        contents=file.read()
        for number in contents.split():
            numbers.append(int(number))

    
    return max(numbers)




if __name__=="__main__":
   
    print(largest(numbers))



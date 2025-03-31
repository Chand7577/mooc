# Write your solution here

def times_ten(start_index:int,end_index:int):
    dic={}

    for value in range(start_index,end_index+1):
        dic[value]=value*10

    return dic




if __name__=="__main__":
    print(times_ten(3,6))
   
# Write your solution here

def create_tuple(*args):
   
    numbers=[value for value in args]

    new_tuple=(min(numbers),max(numbers),sum(numbers))
    return new_tuple





if __name__=="__main__":
    print(create_tuple(5,3,-1))
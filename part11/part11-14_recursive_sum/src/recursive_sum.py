# WRITE YOUR SOLUTION HERE:

def recursive_sum(number:int):
    if number<=1:
        return number


    """ 1+2+3...5  
        sum=5+4...1
        sum=4+3...1
        sum=3+2+1
        recusive equation would be currentNum+recursive_call(currentNum-1)
     """

    result=number+recursive_sum(number-1)
    return result



if __name__=="__main__":

    result = recursive_sum(3)
    print(result)

    print(recursive_sum(5))
    print(recursive_sum(10))

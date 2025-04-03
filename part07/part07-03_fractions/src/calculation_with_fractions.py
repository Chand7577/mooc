from fractions import *


def fractionate(amount:int):
    fracs_list=[ Fraction(1,amount) for _ in range(amount)]
    return fracs_list

   
if __name__=="__main__":
    for value in fractionate(3):
        print(value)
    print(fractionate(5))

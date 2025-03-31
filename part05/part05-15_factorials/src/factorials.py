# Write your solution here


def getFactorials(n):
    if n==0:
        return 1
    
    return n*getFactorials(n-1)


def factorials(n:int):
    fac={}
    for value in range(1,n+1):
        value_of_fac=getFactorials(value)
        fac[value]=value_of_fac

    return fac




if __name__ == "__main__":
    dic=factorials(3)
    print(dic)
    
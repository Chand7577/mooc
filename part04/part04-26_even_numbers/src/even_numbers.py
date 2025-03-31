# Write your solution here


def even_numbers(nums):
    evens=[]

    for value in nums:
        if value%2==0:
            evens.append(value)

    return evens



if __name__=="__main__":
    print(even_numbers([1,2,3,4,5]))
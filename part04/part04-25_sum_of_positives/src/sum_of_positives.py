# Write your solution here


def sum_of_positives(nums):
    result=0

    for value in nums:
        if value>0:
            result+=value

    return result



if __name__=="__main__":

    output=sum_of_positives([2,3,-1])


    print(f"The result is {output}")

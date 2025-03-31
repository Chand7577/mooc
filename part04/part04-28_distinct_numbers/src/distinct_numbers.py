# Write your solution here
def distinct_numbers(nums):
    
    numbers_set=set()

    for value in nums:
        numbers_set.add(value)

  
    return (sorted(list(numbers_set)))







if __name__=="__main__":
  
  
    print(distinct_numbers([3,2,2,1,3,3,1]))
# Write your solution here


def longest_series_of_neighbours(list1):

  max_length=1
  current_length=1


  for value in range(1,len(list1)):
    if abs(list1[value]-list1[value-1])==1:
        current_length+=1
    
    else:
        max_length=max(max_length,current_length)
        current_length=1 # this will reset the value for the new subsequence


  return max(max_length,current_length)


if __name__=="__main__":
    print(longest_series_of_neighbours([1,2,5,4,3,4]))
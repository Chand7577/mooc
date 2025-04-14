# WRITE YOUR SOLUTION HERE:
from collections import Counter

class ListHelper:
   
    @classmethod
    def greatest_frequency(cls,my_list:list):
        freq=Counter(my_list)
        print(freq)
        my_list=set(my_list)
        max_freq=-1
        max_key=0

        for key in my_list:
            if freq[key]>max_freq:
                max_freq=freq[key]
                max_key=key

        return max_key



    @classmethod
    def doubles(cls,my_list:list):
        
        return len([x for x in set(my_list) if my_list.count(x)>1])


if __name__=="__main__":
    numbers =[1, 1, 1, 2, 2, 3]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

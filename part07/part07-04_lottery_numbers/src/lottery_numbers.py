# Write your solution here
from random import sample


def lottery_numbers(amount:int,lower:int,upper:int):
    number_pool = list(range(lower,upper))
   
    weekly_draw = sample(number_pool, amount)
    if len(weekly_draw)>1:
        weekly_draw.sort()
    
    return weekly_draw





if __name__=="__main__":
    for value in lottery_numbers(1,1,10):
        print(value)

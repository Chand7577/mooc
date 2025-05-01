# Write your solution here
import re

def is_dotw(my_string:str):
    expression="Mon|Tue|Wed|Thu|Fri|Sat|Sun"

    return bool(re.fullmatch(expression,my_string))


def all_vowels(my_string:str):
    expression="[aeiou]+"
    return bool(re.fullmatch(expression,my_string))

def time_of_day(my_string:str):
    expression=r'(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])'
    return bool(re.fullmatch(expression,my_string))

if __name__=="__main__":
    # print(all_vowels("eioueioieoieou"))
    # print(all_vowels("autoooooo"))
    # print(time_of_day("12:43:01"))
    # print(time_of_day("AB:01:CD"))
    # print(time_of_day("17:59:59"))
    # print(time_of_day("33:66:77"))
    print(time_of_day("23:55:59"))

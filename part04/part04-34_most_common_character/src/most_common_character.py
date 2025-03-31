# Write your solution here

def most_common_character(string):

    # dic={}
    
   

    # for letter in string:
    #     if letter not in dic:
    #         dic[letter]=1

    #     else:
    #         dic[letter]+=1

    
    # return max(dic,key=dic.get)

    # second solution 
    max_char=""
    max_count=0

    for letter in set(string):
        current_count=string.count(letter)
        if current_count>max_count:
            max_count=current_count
            max_char=letter

    return max_char
    # print(dic.keys())
    # print(max_value)
   
    


if __name__=="__main__":
    print(most_common_character("exemplaryelementary"))
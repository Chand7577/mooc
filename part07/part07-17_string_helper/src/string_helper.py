# Write your solution here


def change_case(orig_string:str):    
    return orig_string.swapcase()


def check_odd_chars(orig_string):
    return  True if len(orig_string)%2!=0 else False



def split_in_half(orig_string:str):
    # if check_odd_chars(orig_string):
    half=len(orig_string)//2
        
     
    first_half=orig_string[0:half]
    second_half=orig_string[half:]

    return (first_half,second_half)

    
    # else:
        # half=len(orig_string)//2
      
        # first_half=orig_string[0:half]
        # second_half=orig_string[half:]

        # return (first_half,second_half)



def remove_special_characters(orig_string:str):
    new_version=""
    for word in orig_string.split():
        new_word=""

        for letter in word:
            if letter.isalnum() or letter==" ":
                new_word+=letter
        
        
        new_version+=new_word+" "
    
    
    return new_version.strip()




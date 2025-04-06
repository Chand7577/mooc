# Write your solution here
from datetime import date
def check_dob(dob:str,marker:str):
    
    try:
        day = dob[:2]
        month = dob[2:4]
        year_suffix = dob[4:]

        if marker == '+':
            year = 1800 + int(year_suffix)
        elif marker == '-':
            year = 1900 + int(year_suffix)
        elif marker == 'A':
            year = 2000 + int(year_suffix)
        else:
            return False

        dob = date((year), int(month), int(day))
        return True
    except:
        return False
    
    

def valid_control(control_char:str,nine_digit_num:str):
    mix_string="0123456789ABCDEFHJKLMNPRSTUVWXY"
   
    index=int(nine_digit_num)%31
    
    
    if len(mix_string)-1<index:
        return False
    
    elif mix_string[index]!=control_char:
        return False
    
    return True


   

def is_it_valid(pic:str):

    if len(pic)>11:
        return False

    marker=pic[6]
    if marker not in ["+","-","A"]:
        return False
    
   
    dob=pic.split(marker)[0]
    nine_digit_number=dob+pic.split(marker)[1][:-1]
    control_char=pic.split(marker)[1][-1]    

    if not check_dob(dob,marker):
        return False

   

    if not valid_control(control_char,nine_digit_number):
        return False
    
    return True
    


if __name__=="__main__":
    print(is_it_valid("100400A644E"))

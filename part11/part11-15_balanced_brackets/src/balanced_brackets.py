
def balanced_brackets(my_string: str):
    new_string=""
    for char in my_string:
        if char in "[]()":
            new_string+=char


    my_string=new_string


    if len(my_string) == 0:
        return True
    
    if my_string[0]=="(":
        if not (my_string[0] == '(' and my_string[-1] == ')'):
            return False
    else:
        if not (my_string[0]=='[' and my_string[-1]==']'):
        
            return False
    # remove first and last character
    return balanced_brackets(my_string[1:-1])



if __name__=="__main__":
    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)


# Write your solution here
import string


# referred this documentation https://docs.python.org/3/library/string.html#string.ascii_lowercase
def separate_characters(my_string: str):
    lower_plus_uppercase=""
    special_operators=""
    other_chars=""
    
    for letter in my_string:
        if letter in string.ascii_letters:
            lower_plus_uppercase+=letter
        
        elif letter in string.punctuation:
                special_operators+=letter

        else:
             other_chars+=letter
             

    return (lower_plus_uppercase,special_operators,other_chars)


if __name__=="__main__":
    parts=separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])

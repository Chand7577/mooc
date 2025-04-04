from random import sample, randint, shuffle
import string


def getNumbers(number: int):
    numbers = [value for value in string.digits]
    numbers = sample(numbers, number)
    return "".join(numbers)


def getSpecialChars(number: int):
    special = ["!", "?", "=", "+", "-", "(", ")", "#"]
    special = sample(special, number)
    return "".join(special)


def getLowerCaseLetters(number: int):
    alphabets = [chr(letter) for letter in range(97, 123)]
    alphabets = sample(alphabets, number)
    return "".join(alphabets)


def generate_strong_password(length: int, bool1: bool, bool2: bool):
 
    #required_parts=1number+1special+reaminglowercase
    #then i can shuffle the values inside a list
    #using join->combine the list into a string
    
    password=""
    current_length=0
    
    #reserve 1 space for nums
    
    if bool1:
        num_length=1
        part1=getNumbers(num_length)
        password+=part1
        current_length+=num_length
        
    #reseve ateast 1 space for special
    if bool2:
        special_length=1
        part2=getSpecialChars(special_length)
        password+=part2
        current_length+=special_length
        
    
    remainin_space_length=length-current_length
    part3=getLowerCaseLetters(remainin_space_length)
    password+=part3
    
    final_password=list(password)
    shuffle(final_password)
    
    return "".join(final_password)

    


if __name__ == "__main__":
    print(generate_strong_password(5, False, True))

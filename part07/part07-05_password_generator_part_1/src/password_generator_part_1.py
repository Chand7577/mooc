# Write your solution here
from random import sample

def generate_password(number:int):
    alphabets=[chr(letter) for letter in range(97,123)]

    password=sample(alphabets,number)
    return "".join(password)

if __name__=="__main__":
    for _ in range(10):
        print(generate_password(8))

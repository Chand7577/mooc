def palindromes(word: str) -> bool:
    return word == word[::-1]

def main():
    word = input("Please type in a palindrome: ")
    
    while not palindromes(word):  
        print("that wasn't a palindrome")
        word = input("Please type in a palindrome: ")
    
    print(f"{word} is a palindrome!")

# if __name__ == "__main__":   
main() 

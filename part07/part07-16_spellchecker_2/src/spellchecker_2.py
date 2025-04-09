# Write your solution here
from difflib import get_close_matches



def check_spell(text:str):
    words=getWords()
    checked_sentence=[]
    for word in text:
        
        
        if word.lower() not in words:
            checked_sentence.append(f"*{word}*")
            

        else:
            checked_sentence.append(f"{word}")

    return " ".join(checked_sentence)



def getWords():
    words=set()  # to store the unique words

    with open('wordlist.txt') as file:
        for word in file:
            letter=word[0]
            word=word.replace("\n","")
            if word not in words:
                words.add(word)

    return words


def get_suggestions(wordlist:set,misspelled:str):
 
    return get_close_matches(misspelled,wordlist)


wordlist=getWords()
user_input=input("write text").split()
print(check_spell(user_input))
print('suggestions:')
for word in check_spell(user_input).split():
    if "*" in word:
        word=word.strip("*")
        print(f"{word}: {', '.join(get_suggestions(wordlist,word))}")
            


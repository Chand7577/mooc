# write your solution here

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

   




def main():
    text=input("Write text:").split()
    print(check_spell(text))


main()
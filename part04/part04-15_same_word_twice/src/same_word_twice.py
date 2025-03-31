# Write your solution here


def getTypedWords():
    words=[]
    word=input("Word:")
    word=word.lower()

    while True:
        if word in words:
            break
        else:
            words.append(word)

        word=input("Word:")
    
    print(f"You typed in {len(words)} different words")

getTypedWords()

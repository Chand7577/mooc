
from random import sample
def getWords(n:int,word_list:list,start:str):

    return sample(word_list,n)



def words(n: int, beginning: str):
    word_list = []

    with open('words.txt') as file:
        for word in file:
            if word.startswith(beginning):
                word_list.append(word.strip())
  
    
    
    if len(word_list)<n:
        raise ValueError("Couldnt'find words atleast  the expected length ")
    
    else:
        return getWords(n,word_list,beginning)

if __name__=="__main__":
    word_list=words(2,"ca")
    for word in word_list:
        print(word)

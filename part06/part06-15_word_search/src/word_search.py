# Write your solution here
import re
def generateRegx(search_term:str):
    pattern=""
    if "*" in search_term:
        if search_term[0]=="*":
            pattern=re.compile(f".*{search_term[1:]}")
                
    
        else:
            pattern=re.compile(f"{search_term[:len(search_term)-1]}.*")
    print(pattern)
    if '.' in search_term:
        pattern=re.compile(f"{search_term}")

    return pattern 





def find_words(search_term:str):

    words=[]
    with open('words.txt') as file:
        for line in file:
            word=line.strip()

            pattern=generateRegx(search_term)
            if pattern!="":
                if pattern.fullmatch(word):
                    words.append(word) 

            if word ==search_term:
                words.append(word)





    return words


if __name__=="__main__":
    print(find_words('reson*'))
# WRITE YOUR SOLUTION HERE:

def most_common_words(filename:str,lower_limit:int):
    data = open(filename).read().replace('\n', ' ').replace('.', '').replace(',', ' ').replace('  ', ' ')
    data=data.split()

    return {word:data.count(word) for word in data if data.count(word)>=lower_limit}
               
                
if __name__=="__main__":

    print(most_common_words("comprehensions.txt",3))

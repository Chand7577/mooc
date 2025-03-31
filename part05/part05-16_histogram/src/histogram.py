# Write your solution here






def histogram(string:str):

    occurences={}
    for letter in string:
        if letter not in occurences:
            occurences[letter]=1
        
        else:
            occurences[letter]+=1

   
    for key,value in occurences.items():
        print(f"{key} {'*'*value}")





if __name__=="__main__":
    histogram('abba')
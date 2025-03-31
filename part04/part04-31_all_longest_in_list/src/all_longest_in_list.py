# Write your solution here

def all_the_longest(list1):

    longest_strings=[]
    max_length=max(len(s) for s in list1)
    
    for word in list1:
        if len(word)==max_length:
            longest_strings.append(word)
    
    return (longest_strings)
  
    

if __name__=="__main__":
    all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])
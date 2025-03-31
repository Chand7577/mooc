# Write your solution here




def invert(s):
    new_dic={}
    for key,value in s.items():
        new_dic[value]=key


   
    s.clear()
    
    #copying values from new_dic to s
    for key,value in new_dic.items():
        s[key]=new_dic[key]
    
    






if __name__=="__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
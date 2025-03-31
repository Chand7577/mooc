# Write your solution here


def no_shouting(list1):
    no_shouting_list=[]

    for word in list1:
        if not (word.isupper()):
            no_shouting_list.append(word)


    return no_shouting_list



if __name__=="__main__":
    print(no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]))    
# Write your solution here


def length_of_longest(strings):

    for value in range(len(strings)):
        strings[value]=len(strings[value])


    return max(strings)




if __name__=="__main__":
    print(length_of_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))
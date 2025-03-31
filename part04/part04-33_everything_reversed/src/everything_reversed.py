# Write your solution here


def everything_reversed(list1):
    reversed_list=[]
    for word in list1:
        reversed_list.append(word[::-1])

    return (reversed_list[::-1])


if __name__=="__main__":
    print(everything_reversed(["Amrit","chand"]))
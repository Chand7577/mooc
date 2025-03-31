# Write your solution here


def list_sum(list1,list2):
    list3=[]


    for value in range(len(list1)):
        list3.append(list1[value]+list2[value])

    return list3







if __name__=="__main__":
    print(list_sum([1,2,3],[7,8,9]))
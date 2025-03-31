# Write your solution here



def older_people(people:list,year:int):
    ages=[age[1] for age in people ]
   


    older_people=[]

    for person in people:
        if person[1]<year:
            older_people.append(person[0])

    return older_people


if __name__=="__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(older_people(people,1979))
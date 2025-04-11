# Write your solution here


def smallest_average(person1:dict,person2:dict,person3:dict):
    average_results=[]
    people=[person1,person2,person3]
  
    for current_person in people:
        result=current_person["result1"]+current_person['result2']+current_person['result3']
        average_results.append(result/3)
        current_person['avg']=result/3

    
    min_result=min(average_results)

    for current_person in people:
        if current_person['avg']==min_result:
            del current_person['avg']
            return current_person





if __name__=="__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))

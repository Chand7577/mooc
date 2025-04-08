# Write your solution here

import json


def print_persons(filename:str):
    with open(filename) as file:
        data=file.read()


    students_info=json.loads(data)


    for student in students_info:
        
        name,age=student["name"],student["age"]
        hobbies=student["hobbies"]
        
        print(f"{name} {age} years ({', '.join(hobbies)})")


if __name__=="__main__":
    print_persons("file1.json")


    

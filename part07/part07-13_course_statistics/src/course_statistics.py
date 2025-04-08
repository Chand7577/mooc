# Write your solution here
import urllib.request
import json
import math

def check_active(course):
    return True if course["enabled"] else False



def getData():
    request=urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses ")
    data=request.read()
    course_info=json.loads(data)   


    return course_info

    

def retrieve_all():
    course_info=getData()
    active_courses=[]

    for course in course_info:
        if check_active(course):
            active_courses.append(course)


    #for course in active_courses:
    extracted_part=[(course["fullName"],course["name"],course["year"],sum(course['exercises'])) for course in active_courses]
        # extracted_part.append(course['fullName'])
        # extracted_part.append(course["name"])
        # extracted_part.append(course["year"])
        # extracted_part.append(sum(course['exercises']))

    return extracted_part

def retrieve_course(course_name:str):

    data_course={}

    address=f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    request=urllib.request.urlopen(address)
    data=request.read()
    weekly_data_course=json.loads(data)

    

    data_course["weeks"]=len(weekly_data_course)
    
    max_students=max([ course_info['students'] for key,course_info in weekly_data_course.items()])
    data_course['students']=max_students
    
    total_hours=sum([course_info['hour_total'] for key,course_info in weekly_data_course.items()])
    data_course['hours']=total_hours

    hours_average=math.floor(total_hours/max_students)
    data_course['hours_average']=hours_average

    total_exercises=sum([course_info['exercise_total'] for key,course_info in weekly_data_course.items()])
    data_course['exercises']=total_exercises

    average_exercises=math.floor(total_exercises/max_students)
    data_course['exercises_average']=average_exercises


    return data_course

if __name__=="__main__":

    # courses=retrieve_all()
    # print(courses)

    retrieve_course('docker2019')




    
        
        




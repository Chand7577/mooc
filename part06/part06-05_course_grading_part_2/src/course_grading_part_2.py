# write your solution here

def convert_string_to_int(numbers:list):
    for number in range(len(numbers)):
        numbers[number]=int(numbers[number])

    return numbers
   
def getTotalCompletedCourses(list1):
    
   
    numbers=convert_string_to_int(list1)
   
    return sum(numbers)



def getExamPoints(points:list,key):
    numbers=points.get(key)
    return sum(numbers)


def files_to_process():
    student_info_file=input("Student information:").strip().lower()
    exercise_data=input("Exercises completed:").strip().lower()
    exam_points_data=input("Exam points:").strip().lower()
    

    student_info={}
    with open(student_info_file) as file:
        for line in file:
            line=line.split(';')
            if line[0]=="id":  #ignore the header
                continue
            student_info[line[0]]=(line[1],line[2].strip())

    
    exercise_info={}
    with open(exercise_data) as file:
        for line in file:
            line=line.strip().split(";")
            if line[0]=="id":  #ignore the header
                continue
            
            
                
            exercise_info[line[0]]=getTotalCompletedCourses(line[1:])

    # # print()
    exam_points={}
    with open(exam_points_data) as file:
        for line in file:
            line=line.strip().split(";")
            if line[0]=="id":
                continue
          
            exam_points[line[0]]=convert_string_to_int(line[1:])


    for key,values in student_info.items():
            total_points=getExamPoints(exam_points,key)+(exercise_info[key]//4)
          

            if total_points<=14:
                print(f"{student_info[key][0]} {student_info[key][1]} 0")

            elif total_points<=17:
                print(f"{student_info[key][0]} {student_info[key][1]} 1")
            
            elif total_points<=20:
                print(f"{student_info[key][0]} {student_info[key][1]} 2")
            
            elif  total_points<=23:
                print(f"{student_info[key][0]} {student_info[key][1]} 3")
            
            elif total_points<=27:
                print(f"{student_info[key][0]} {student_info[key][1]} 4")

            else:
                print(f"{student_info[key][0]} {student_info[key][1]} 5")


    #     print(f"{student_info[key][0]} {student_info[key][1]} {exercise_info[key]}")
    
   
files_to_process()
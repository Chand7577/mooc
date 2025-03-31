# write your solution here


def getTotalCompletedCourses(list1):
    
   
    for number in range(len(list1)):
        list1[number]=int(list1[number])

   
    return sum(list1)

def files_to_process():
    student_info_file=input("Student information:").strip().lower()
    exercise_data=input("Exercises completed:").strip().lower()
    

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
    for key,values in student_info.items():
        print(f"{student_info[key][0]} {student_info[key][1]} {exercise_info[key]}")
files_to_process()
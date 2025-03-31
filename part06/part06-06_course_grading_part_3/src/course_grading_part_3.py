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

def stats(name, completed, exercise_points, examPoints, total_points, grade, count):
    if count == 1:
        # Print the header with precise alignment
        print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':110}")
    
    full_name = f"{name[0]} {name[1]}"
    
    # Align columns exactly as in the example
    print(f"{full_name:<30}{completed:<10}{exercise_points:<10}{examPoints:<10}{total_points:<10}{grade:<10}")

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

    exam_points={}
    with open(exam_points_data) as file:
        for line in file:
            line=line.strip().split(";")
            if line[0]=="id":
                continue
          
            exam_points[line[0]]=convert_string_to_int(line[1:])

    count=0
    for key,values in student_info.items():
            examPoints=getExamPoints(exam_points,key)
            exercise_points=(exercise_info[key]//4)
            total_points=examPoints+exercise_points
            count+=1
            grade=""

            if total_points<=14:
                grade=0
            elif total_points<=17:
                grade=1
            elif total_points<=20:
                grade=2
            elif total_points<=23:
                grade=3
            elif total_points<=27:
                grade=4
            else:
                grade=5

            stats(student_info[key], exercise_info[key], exercise_points, examPoints, total_points, grade, count)

files_to_process()
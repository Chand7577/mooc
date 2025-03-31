# tee ratkaisu tänne
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

def stats(name, completed, exercise_points, examPoints, total_points, grade, count,course,key):

    full_name = f"{name[0]} {name[1]}"
    courseTitle=""
    credits_=""
    if count==1:
        with open(course) as file:
            for line in file:
                line=line.strip()
                if "credits" in line:
                    credits_+=line[len(line)-2:]

                else:
                    courseTitle+=line[5:]
        
   

    
    mode='w' if count==1 else 'a'
    with open('results.txt',mode) as file2:  #adding course result to results.txt
        if count==1:
            file2.write(f"{courseTitle.strip()},{credits_} credits\n")
            file2.write(f"======================================\n")   
            file2.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':110}\n")
        
        
        
        file2.write(f"{full_name:<30}{completed:<10}{exercise_points:<10}{examPoints:<10}{total_points:<10}{grade:<10}\n")
    mode='w' if count==1 else 'a'
    with open('results.csv',mode) as file3: # write into results.csv
        file3.write(f"{key};{full_name};{grade}\n")



def files_to_process():
    student_info_file=input("Student information:").strip().lower()
    exercise_data=input("Exercises completed:").strip().lower()
    exam_points_data=input("Exam points:").strip().lower()
    course=input("Course information:")
    print(f"Results written to files results.txt and results.csv")
    
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

            stats(student_info[key], exercise_info[key], exercise_points, examPoints, total_points, grade, count,course,key)

files_to_process()
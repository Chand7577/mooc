# Write your solution

class Course:
    def __init__(self):
        self.courses={}


    def add_course_info(self,course:str,grade:int,cred:int):
        
        if course not in self.courses:
            self.courses[course]={
                "grade":{

                },
                "credit":{

                }
            }

            self.courses[course]["grade"]=grade
            self.courses[course]["credit"]=cred

        else:
            if self.courses[course]["grade"]<grade: 
                self.courses[course]["grade"]=grade

            if self.courses[course]["credit"]<cred:
                self.courses[course]["credit"]=cred


    def get_course_data(self,course:str):
        if course not in self.courses:
            print("no entry for this course")
            return 

        grade=self.courses[course]["grade"]
        credit=self.courses[course]["credit"]

        print(f"{course} ({credit} cr) grade {grade}")
        



class CourseBookApplication:
    def __init__(self):
        self.__course=Course()


    def option(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")


    def add_course(self):
        course=input("course:")
        grade=int(input("grade:"))
        creds=int(input("credits:"))

        self.__course.add_course_info(course,grade,creds)


    
    def get_course_data(self):
        course=input("course:")
        self.__course.get_course_data(course)

    def getTotalCredits(self,courses:Course):
        return sum([courses[course]["credit"] for course in courses])
    
    
    def getMean(self,courses:Course):
        grades=[courses[course]['grade'] for course in courses]
        return sum(grades)/len(grades)
    
    def statistics(self):
        total_credits=self.getTotalCredits(self.__course.courses)
        mean=self.getMean(self.__course.courses)

        print(f"{len(self.__course.courses)} completed courses, a total of {total_credits} credits")
        print(f"mean {round(mean,1)}")
        print('grade distribution')

        for current_row in range(5,0,-1):
            total_courses=0
            for key in self.__course.courses:
                
                if self.__course.courses[key]["grade"]==current_row:
                    total_courses+=1
                    
            print(f"{current_row}: {'x'*total_courses}")
            
        


    def execute(self):
        self.option()

        while True:

            command=int(input('command:'))
            if command==1:
                self.add_course()

            elif command==2:
                self.get_course_data()

            elif command==3:
                self.statistics()

            else:
                break



App=CourseBookApplication()
App.execute()

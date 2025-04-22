from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution


def sum_of_all_credits(credits:list):

    result=reduce(lambda reducedSum,course:reducedSum+course.credits,credits,0)
    return result

def sum_of_passed_credits(credits:list):
    filteredlist=list(filter(lambda course:course.grade>=1,credits))
    result=reduce(lambda reducedSum,course:reducedSum+course.credits,filteredlist,0)
    return result


def average(credits:list):
    filteredlist=list(filter(lambda course:course.grade>=1,credits))
    result=reduce(lambda reducedSum,course:reducedSum+course.grade,filteredlist,0)
    return result/len(filteredlist)

if __name__=="__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    

    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

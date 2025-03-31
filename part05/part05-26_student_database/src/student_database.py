def add_student(students: dict, name: str):
    students[name] = {'courses': []}  # Dictionary for each student with courses


def add_course(students: dict, name: str, course: tuple):
    if name not in students:
        return

    course_name, grade = course
    if grade == 0:  # Ignore invalid courses
        return
    
    for i, (existing_course, existing_grade) in enumerate(students[name]['courses']):
        if existing_course == course_name:
            if grade > existing_grade:  # Update only if the grade is higher
                students[name]['courses'][i] = (course_name, grade)
            return  # Exit function

    students[name]['courses'].append(course)


def total_grade(courses: list):
    return sum(1 for course in courses if course[1] > 0)


def get_grade(courses: list):
    length = total_grade(courses)
    if length == 0:
        return 0  # Prevent division by zero
    
    return sum(course[1] for course in courses) / length


def get_details(name, student):
    print(f"{name}:")
    if not student["courses"]:
        print(" no completed courses")
    else:
        print(f"{len(student['courses']):>2} completed courses:")
        for course in student["courses"]:
            print(f"  {course[0]} {course[1]}")
        print(f"{'average grade':>14} {get_grade(student['courses']):.1f}")


def print_student(students, name):
    if name not in students:
        print(f"{name}: no such person in the database")
    else:
        get_details(name, students[name])


def get_average_grade(students: dict):
    if not students:
        print("No students in the database")
        return
    
    max_grade = 0
    person_with_max_grade = ""

    for key, value in students.items():
        avg_grade = get_grade(value['courses'])
        if avg_grade > max_grade:
            max_grade = avg_grade
            person_with_max_grade = key

    print(f"best average grade {max_grade:.1f} {person_with_max_grade}")


def summary(students: dict):
    if not students:
        print("No students in the database")
        return
    
    print(f"students {len(students)}")

    most_courses_completed = max(students.items(), key=lambda x: len(x[1]['courses']), default=(None, None))
    
    if most_courses_completed[0]:
        name_student = most_courses_completed[0]
        max_course = len(most_courses_completed[1]['courses'])
        print(f"most courses completed {max_course} {name_student}")
    
    get_average_grade(students)


if __name__ == "__main__":
    students = {}
    
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 1))
    add_course(students, "Peter", ("Software Development Methods", 5))  # Updates grade if higher
    add_course(students, "Peter", ("Data Structures", 4))
    print_student(students, "Peter")
    summary(students)
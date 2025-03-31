# Write your solution here

def getAverage(results):
    totalScores = sum(sum(result) for result in results)
    return round(totalScores / len(results), 1) if results else 0.0


def getPassPercent(results):
    passed_students = 0

    for result in results:
        if result[0] >= 10 and (result[0] + result[1]) >= 15:
            passed_students += 1

    return round((passed_students / len(results)) * 100, 1) if results else 0.0


def showGradeDistro(results):
    grades = {i: 0 for i in range(6)}

    for result in results:
        total = result[0] + result[1]
        if result[0] < 10:
            grades[0] += 1
        elif total <= 14:
            grades[0] += 1
        elif total <= 17:
            grades[1] += 1
        elif total <= 20:
            grades[2] += 1
        elif total <= 23:
            grades[3] += 1
        elif total <= 27:
            grades[4] += 1
        else:
            grades[5] += 1

    print("Grade distribution:")
    for grade in range(5, -1, -1):
        if grades[grade] > 0:
            print(f"  {grade}: {'*' * grades[grade]}")
        else:
            print(f"  {grade}:")


def takeInputs():
    results = []
    
    while True:
        input_value = input("Exam points and exercises completed: ")

        if input_value == "":
            break

        exam, exercise = map(int, input_value.split())
        results.append([exam, exercise // 10])  # Convert exercises to exercise points

    return results


def main():
    results = takeInputs()
    print("Statistics:")
    average = getAverage(results)
    print(f"Points average: {average}")
    percent = getPassPercent(results)
    print(f"Pass percentage: {percent}")
    showGradeDistro(results)


main()

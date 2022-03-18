def gradingStudents(grades):
    copyArr = []

    for _ in grades:
        temp = _
        if temp < 40:
            if temp == 38:
                temp += 2
            if temp == 39:
                temp += 1
        elif temp % 5 == 3:
            temp += 2
        elif temp % 5 == 4:
            temp += 1
        else:
            temp = temp
        copyArr.append(temp)

    return copyArr


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

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
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

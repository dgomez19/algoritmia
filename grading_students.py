#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'grading_students' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def grading_students(grades):
    
    new_grades = []
    for i in grades:
        next_multiple = ((i + 4) // 5) * 5
        if (next_multiple - i) < 3 and i >= 38:
            new_grades.append(next_multiple)
        else:
            new_grades.append(i)
    return new_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = grading_students(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

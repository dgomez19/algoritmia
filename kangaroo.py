#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v2 > v1:
        return 'NO'
        
    if x2 > x1 and v1 == v2:
        return 'NO'
    
    canguro1 = x1 + v1
    canguro2 = x2 + v2
    condicion = False
    result = None
    while condicion == False:
        x1 = canguro1
        x2 = canguro2
        
        if canguro1 > canguro2:
            result = 'NO'
            condicion = True
        elif canguro1 == canguro2:
            result = 'YES'
            condicion = True
        
        canguro1 = x1 + v1
        canguro2 = x2 + v2


    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

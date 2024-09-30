#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratory_birds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratory_birds(arr):
    aux, res = 0, 0
    dic = {}
    for i in sorted(arr):

        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1

    for i in dic:
        if aux < dic[i]:
            aux = dic[i]
            res = i

    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratory_birds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

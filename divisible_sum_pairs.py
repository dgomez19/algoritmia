#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisible_sum_pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisible_sum_pairs(n, k, ar):
    count = 0
    count_result = 0

    for i in range(n):
        for x in range(n):
            if x != i and i < x:
                suma = ar[x] + ar[i]
                
                if suma % k == 0:
                    count_result += 1

        count += 1
    print(count_result)
    return count_result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisible_sum_pairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

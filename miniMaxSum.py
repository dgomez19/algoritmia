#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    total_suma = sum(arr)
    
    valor_minimo = total_suma - max(arr)
    valor_maximo = total_suma - min(arr)
    
    print(valor_minimo, valor_maximo)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

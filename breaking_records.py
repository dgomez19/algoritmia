#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breaking_records' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breaking_records(scores):
    ultima_mala = 0
    ultima_buena = 0
    
    contar_buenas = 0
    contar_malas = 0

    for i in range(len(scores)):
        if i == 0:
            ultima_buena, ultima_mala = scores[i], scores[i]
        else:
            if scores[i] > ultima_buena:
                contar_buenas += 1
                ultima_buena = scores[i]
            elif scores[i] < ultima_mala:
                ultima_mala = scores[i]
                contar_malas += 1
                
        
    print(contar_buenas, contar_malas)
        
    return contar_buenas, contar_malas

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breaking_records(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

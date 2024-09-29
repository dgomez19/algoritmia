#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    nueva_hora = s        

    if 'PM' == s[-2:] and int(s[0:2]) != 12:
        nueva_hora = int(s[0:2]) + 12
        nueva_hora = f'{nueva_hora}{s[2:8]}'
    elif 'PM' == s[-2:] and int(s[0:2]) == 12:
        nueva_hora = nueva_hora[:-2]
        
    if 'AM' == s[-2:] and int(s[0:2]) == 12:
        nueva_hora = f'00{s[2:8]}'
    elif 'AM' == s[-2:] and int(s[0:2]) != 12:
        nueva_hora = nueva_hora[:-2]

    return nueva_hora

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

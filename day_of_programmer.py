#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
#
# Complete the 'day_of_programmer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def day_of_programmer(year):
    
    day_programmer = 256
    months = [31, 28, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31] # Calendario original
    
    if year < 1918: # Es Juliano
        if year % 4 == 0: # Es bisiesto
            months = [31, 29, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31] # Calendario editado

    if year > 1918: # Es Gregoriano 
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            months = [31, 29, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31] # Calendario editado

    if year == 1918:
        months = [31, 15, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31] # Calendario original

    suma = 0
    result = 0
    month = 0

    for i in range(len(months)):
        suma += months[i]

        if suma >= day_programmer:
            result = suma - day_programmer
            result = months[i] - result
            month = i
            break

    month = month + 1
    month = str(month).zfill(2)
    return f'{result -1}.{month}.{year}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = day_of_programmer(year)

    fptr.write(result + '\n')

    fptr.close()

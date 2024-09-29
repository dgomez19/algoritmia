#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbing_leader_board' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbing_leader_board(ranked, player):

    ranked = sorted(set(ranked), reverse=True)
    resultados = []
    
    for puntuacion in player:
        rango = 1
        for score in ranked:
            if puntuacion < score:
                rango += 1
            else:
                break
        resultados.append(rango)
    return resultados


ranked = [50, 40, 100, 20, 10]
player = [5, 25, 50, 120]

result = climbing_leader_board(ranked, player)
print(result)

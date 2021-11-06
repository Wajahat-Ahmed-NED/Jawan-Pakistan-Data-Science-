#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#

def squares(a, b):
    # Write your code here
    sr = 0
    for i in range(a, b + 1):
        if int(math.sqrt(i) + 0.5) ** 2 == i:
            sr = math.sqrt(i)
            break;
    count = 0
    while (sr * sr <= b):
        if (sr * sr >= a):
            count += 1
        sr += 1
    # for i in range(a,b+1):
    #     # print(type(math.sqrt(i)))
    #     if i%10 in [0,1,4,5,6,9] :
    #         if int((math.sqrt(i)) + 0.5) ** 2 == i:
    #             count+=1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()

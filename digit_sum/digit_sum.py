#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here
    one = 1
    sum = 0
    res = [int(n[idx: idx + one]) for idx in range(0, len(n), one)]

    for i in res:
        sum = sum + i

    print(sum)

    print(k, res)
    return

    #  iterate through res ad add each number together

    return 0  # superDigit(varforn, varfork)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
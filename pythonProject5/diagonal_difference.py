#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    # for i in arr:
    #     print(arr[i])
    # print(n - 1)
    # print(arr[0][0],arr[1][1], arr[2][2])

    sum1 = 0
    sum2 = 0
    diff = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # Condition for principal diagonal
            if (i == j):
                sum1 = sum1 + arr[i][j]
                # print("sum1 ", sum1)
                # print(arr[i][j], end = ", ")

    print()

    for i in range(len(arr)):
        for j in range(len(arr)):
            if (i + j == n - 1):
                sum2 = sum2 + arr[i][j]
                # print("sum2 ", sum2)
                # print(arr[i][j], end = ", ")

    if (sum1 > sum2):
        diff = sum1 - sum2
    else:
        diff = sum2 - sum1

    return diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

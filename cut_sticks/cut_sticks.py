#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    # print(n)      #  6
    mini = min(arr)
    # print(mini)      #  2
    # print(len(arr))  # 6 same as n
    # print(arr)       # 5, 4, 4, 3, 3, 8

    counter = n
    print(counter)

    for i in range(n):
        arr[i] = arr[i] - mini
        print(i)
        print("arr is: ", arr)
        if arr[i] > 0:
            counter += 1
            print("counter is: ", counter)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

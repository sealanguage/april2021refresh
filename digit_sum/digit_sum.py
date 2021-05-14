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
    holder = []
    holderStack = []
    count = 0

    # def addToSum():

    #  This works to add the numbers in the initial res
    for count in range(k):  # count is 0 0 0 1 1 1 2 2 2
        for i in res:
            sum = sum + i
            print("count ", count)

            # if sum < 10:
            #     print(sum)
            # else:
            #     sum = res = sum
        print(sum)
        print('res ', res)

        # holderStack.append(i)
        # print("hS ", holderStack)
        # return sum
    # addToSum()

    #     if sum < 10:
    #         print("sum less 10 ", sum)
    # else:
    #     for n in holderStack:
    #         sum = sum + n

    # print("sum = sum + n; ", sum)

    # print("hS2 ", holderStack)

    # print(k, res)

    # for val in range(sum):
    #     holderStack.append(val)
    # print(holderStack)
    # for i in range(sum):
    #     holder.append(i)
    # check = len(str(sum))
    # if check > 1:
    #     return
    # write this as a function then call the function again here till check length is 1

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

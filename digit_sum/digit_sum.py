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
    # holder = []
    # holderStack = []
    count = 0
    print(k, res)
    contained = res
    print('contained ', contained)

    # def addToSum():

    #  This works to add the numbers in the initial res
    for count in range(k):  # count is 0 0 0 1 1 1 2 2 2, getting input 3 times
        for i in contained:
            sum = sum + i
            print("count ", count)

            if sum < 10:
                print(sum)
            else:
                print('sum more than 10')
                # [int(i) for i in str(12345)]
                #  list(str(12345))
                res = list(str(sum))
        print(res)
        print('contained ', contained)

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

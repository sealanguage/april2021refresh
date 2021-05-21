#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # n = int(input().strip())

    # original code
    # n = bin(n)
    # n = bin(n)[2:].split('0')
    # n = len(n)

    #  after refactoring
    print(len(max(bin(int(input().strip()))[2:].split('0'))))


    # print(n)

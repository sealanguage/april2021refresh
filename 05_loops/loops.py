#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    for number in range(11):
        if number > 0:
            print(n, "x", number, "=", n * number)


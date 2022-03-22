import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    copyN = n - 1
    m = 1
    for i in range(n):
        print(" "*(copyN) + (m*"#"))
        m +=1
        copyN -= 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

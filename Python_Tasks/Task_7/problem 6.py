# problem: Pangrams
# HackerRank Link: https://www.hackerrank.com/challenges/pangrams/problem


import math
import os
import random
import re
import sys


def pangrams(s):
    letters = set(s.lower())
    
    if all(chr(i) in letters for i in range(ord('a'), ord('z') + 1)):
        return "pangram"
    else:
        return "not pangram"

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

# problem: Find the Runner-UP score!
# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

import math
import sys
import re
import random 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])

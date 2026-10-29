# problem : Find the Runner-up Score!
# HackerRank Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

import math
import sys
import re
import random 

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    unique_scores = sorted(set(arr))
    print(unique_scores[-2])

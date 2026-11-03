# problem: Separate the Numbers
# HackerRank Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem


import math
import os
import random
import re
import sys

def separateNumbers(s):
    n = len(s)

    for i in range(1, n // 2 + 1):
        first = s[:i]

        if first[0] == '0':
            continue

        num = int(first)
        result = ""

        while len(result) < n:
            result += str(num)
            num += 1

        if result == s:
            print("YES", first)
            return

    print("NO")


q = int(input())

for _ in range(q):
    s = input()
    separateNumbers(s)






# problem: Weighted Uniform Strings
# HackerRank Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem


import math
import os
import random
import re
import sys


s = input().strip()
n = int(input())

queries = [int(input()) for _ in range(n)]

weights = set()
count = 0
prev = ''

for ch in s:
    if ch == prev:
        count += 1
    else:
        count = 1
        prev = ch

    value = (ord(ch) - ord('a') + 1) * count
    weights.add(value)

for q in queries:
    if q in weights:
        print("Yes")
    else:
        print("No")




# problem: Sherlock and Valid String
# HackerRank Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem


import math
import os
import random
import re
import sys

from collections import Counter

def isValid(s):
    freq = Counter(s)
    counts = Counter(freq.values())

    if len(counts) == 1:
        return "YES"

    if len(counts) > 2:
        return "NO"

    (f1, c1), (f2, c2) = counts.items()

    if f1 == 1 and c1 == 1:
        return "YES"

    if f2 == 1 and c2 == 1:
        return "YES"

    if f1 > f2 and f1 - f2 == 1 and c1 == 1:
        return "YES"

    if f2 > f1 and f2 - f1 == 1 and c2 == 1:
        return "YES"

    return "NO"


s = input().strip()
print(isValid(s))

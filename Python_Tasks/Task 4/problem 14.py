# Problem: Set.add()
#HackerRank Link: https://www.hackerrank.com/challenges/py-set-add/problem

import math
import random 
import re
import sys
n = int(input())
countries = set()

for _ in range(n):
    countries.add(input().strip())

print(len(countries))

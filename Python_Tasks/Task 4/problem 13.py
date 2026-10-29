# problem : Symmetruc Difference 
# HackerRank Link: https://www.hackerrank.com/challenges/symmetric-difference/problem

import math
import sys
import random
import re 

m = int(input())
a = set(map(int, input().split()))

n = int(input())
b = set(map(int, input().split()))

result = sorted(a.symmetric_difference(b))

for num in result:
    print(num)

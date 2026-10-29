# problem: Collections.counter()
# HackerRank Link: https://www.hackerrank.com/challenges/collections-counter/problem

import math
import sys


from collections import Counter

X = int(input())
shoes = Counter(map(int, input().split()))
N = int(input())

total = 0

for _ in range(N):
    size, price = map(int, input().split())

    if shoes[size] > 0:
        total += price
        shoes[size] -= 1

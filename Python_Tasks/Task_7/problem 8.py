# problem: Gemstones
# HackerRank Link: https://www.hackerrank.com/challenges/gem-stones/problem


import math
import os
import random
import re
import sys

def gemstones(arr):
    common = set(arr[0])
    for rock in arr[1:]:
        common = common.intersection(set(rock))
    return len(common)
if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(input().strip())
    result = gemstones(arr)
    print(result)



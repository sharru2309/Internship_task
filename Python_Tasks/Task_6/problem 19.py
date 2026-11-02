# problem: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem


import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()

    freq = Counter(s)

    result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    for char, count in result[:3]:
        print(char, count)
        
        
        

# problem: Mars Exploration
# HackerRank Link: https://www.hackerrank.com/challenges/mars-exploration/problem


import math
import os
import random
import re
import sys
    
def marsExploration(s):
    expected = "SOS"
    count = 0

    for i in range(len(s)):
        if s[i] != expected[i % 3]:
            count += 1
    return count

s = input()
print(marsExploration(s))


# problem: Anagram
# HackerRank Link: https://www.hackerrank.com/challenges/anagram/problem


import math
import os
import random
import re
import sys

def anagram(s):
    n = len(s)
    if n % 2 != 0:
        return -1

    s1 = s[:n // 2]
    s2 = s[n // 2:]

    count = [0] * 26
    for ch in s1:
        count[ord(ch) - ord('a')] += 1
    for ch in s2:
        count[ord(ch) - ord('a')] -= 1
    return sum(x for x in count if x > 0)


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        s = input().strip()
        print(anagram(s))



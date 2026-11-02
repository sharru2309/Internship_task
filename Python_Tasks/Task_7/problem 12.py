# problem: Making Anagrams 
# HackerRank Link: https://www.hackerrank.com/challenges/making-anagrams/problem


import math
import os
import random
import re
import sys

def makingAnagrams(s1, s2):
    count1 = [0] * 26
    count2 = [0] * 26

    for ch in s1:
        count1[ord(ch) - ord('a')] += 1

    for ch in s2:
        count2[ord(ch) - ord('a')] += 1

    deletions = 0

    for i in range(26):
        deletions += abs(count1[i] - count2[i])

    return deletions

if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()

    print(makingAnagrams(s1, s2))



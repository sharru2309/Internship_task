# problem: caesar ciphar
# HackerRank Link: https://www.hackerrank.com/challenges/caesar-cipher-1/problem


import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    result = ""
    k = k % 26

    for ch in s:
        if ch.islower():
            result += chr((ord(ch) - 97 + k) % 26 + 97)
        elif ch.isupper():
            result += chr((ord(ch) - 65 + k) % 26 + 65)
        else:
            result += ch

    return result


n = int(input())
s = input()
k = int(input())

print(caesarCipher(s, k))

# problem: String Construction
# HackerRank Link: https://www.hackerrank.com/challenges/string-construction/problem


def stringConstruction(s):
    return len(set(s))
n = int(input())
for _ in range(n):
    s = input().strip()
    print(stringConstruction(s))



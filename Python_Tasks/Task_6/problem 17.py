# problem: Check String Superset 
# HackerRank Link: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    other_set = set(map(int, input().split()))
    if not A > other_set:
        result = False
        break

print(result)

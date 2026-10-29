# problem : Nested Lists
# HackerRank Link: https://www.hackerrank.com/challenges/nested-list/problem

import math
import re
import sys
import random
if __name__ == '__main__':
    students= []
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name,grade])
grades = sorted(set(student[1] for student in students))
second_lowest = grades[1]

names = sorted(student[0] for student in students if student[1] == second_lowest)

for name in names:
    print(name)

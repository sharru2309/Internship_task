# problem: The Captain's Room 
# HackerRank Link: https://www.hackerrank.com/challenges/py-the-captains-room/problem


import math

k = int(input())
rooms = list(map(int, input().split()))

count = {}

for room in rooms:
    count[room] = count.get(room, 0) + 1

for room, frequency in count.items():
    if frequency == 1:
        print(room)
        break

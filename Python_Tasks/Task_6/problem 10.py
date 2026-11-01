# problem: Designer Door Mat
# HackerRank Link: https://www.hackerrank.com/challenges/designer-door-mat/problem

N, M = map(int, input().split())

# Upper part
for i in range(1, N, 2):
    print(('.|.' * i).center(M, '-'))

# Middle part
print('WELCOME'.center(M, '-'))

# Lower part
for i in range(N - 2, 0, -2):
    print(('.|.' * i).center(M, '-'))

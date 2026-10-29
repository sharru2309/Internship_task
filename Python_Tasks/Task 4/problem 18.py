# problem : Lists
# HackerRank Link: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))

        elif command[0] == "print":
            print(my_list)

        elif command[0] == "remove":
            my_list.remove(int(command[1]))

        elif command[0] == "append":
            my_list.append(int(command[1]))

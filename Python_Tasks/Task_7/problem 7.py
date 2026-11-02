# problem: Alphabet Rangoli
# HackerRank Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem


def print_rangoli(size):
    import string
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(size):
        left = alphabet[size-1:i:-1]
        right = alphabet[i:size]

        pattern = '-'.join(left + right)
        lines.append(pattern.center(4 * size - 3, '-'))

    print('\n'.join(lines[::-1] + lines[1:]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

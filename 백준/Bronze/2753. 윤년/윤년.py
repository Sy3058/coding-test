import sys
input = sys.stdin.readline
a = int(input())
print(1) if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 else print(0)
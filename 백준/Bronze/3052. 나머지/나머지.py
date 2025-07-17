import sys
input = sys.stdin.readline

rest = set()
for _ in range (10):
    num = int(input()) % 42
    rest.add(num)

print(len(rest))

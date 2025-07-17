import sys
input = sys.stdin.readline
num = 0
ni = 0
for i in range (1, 10):
    tmp = int(input())
    if tmp > num:
        num = tmp
        ni = i
print(num)
print(ni)
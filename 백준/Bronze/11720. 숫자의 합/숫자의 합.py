import sys
input = sys.stdin.readline
n = int(input())
num = list(input().strip())
hap = 0
for i in range (n):
    hap += int(num[i])
print(hap)
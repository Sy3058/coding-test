import sys
input = sys.stdin.readline

n = int(input())
a = list(enumerate(list(map(int, input().split()))))
p = [0 for _ in range (n)]

a.sort(key = lambda x:x[1])
for i in range (n):
    p[a[i][0]] = i

print(' '.join(map(str, p)))
import sys
input = sys.stdin.readline

s = input().strip()

ans = []
for i in range (len(s) - 1, -1, -1):
  ans.append(s[i:])

ans.sort()
for x in ans:
  print(x)
import sys
input = sys.stdin.readline

l = int(input())
s = list(map(int, input().split()))
n = int(input())
cnt = 0

s.sort()
for i in range (l):
  if s[i] > n:
    if i == 0:
      a = 0

    else:
      a = s[i-1]
      
    if a == n:
      break

    cnt += s[i]-n-1
    if a < n and a+1 != n:
      cnt += (n-a-1)*(s[i]-n)
    break

print(cnt)
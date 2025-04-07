import sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, list(input().strip()))) # before
a = list(map(int, list(input().strip()))) # after
c = b.copy() # change b

s = {1:0, 0:1} # switch

# 0번 스위치를 누르지 않는다고 가정
cnt = 0
for i in range (1, n):
  if c[i-1] != a[i-1]:
    if i == n-1:
      c[i-1], c[i] = s[c[i-1]], s[c[i]]
    else:
      c[i-1], c[i], c[i+1] = s[c[i-1]], s[c[i]], s[c[i+1]]
    cnt += 1

if c != a:
  cnt = 1 # 0번 스위치를 누름
  b[0], b[1] = s[b[0]], s[b[1]]
  for i in range (1, n):
    if b[i-1] != a[i-1]:
      if i == n-1:
        b[i-1], b[i] = s[b[i-1]], s[b[i]]
      else:
        b[i-1], b[i], b[i+1] = s[b[i-1]], s[b[i]], s[b[i+1]]
      cnt += 1
  
if b != a and c != a:
  print(-1)

else:
  print(cnt)
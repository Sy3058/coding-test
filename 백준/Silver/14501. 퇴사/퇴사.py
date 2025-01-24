import sys
input = sys.stdin.readline

t = []
p = []

n = int(input())
for _ in range (n):
  time, pay = map(int, input().split())
  t.append(time)
  p.append(pay)

tp = [0 for _ in range (n+1)]

for i in range (n):
  if i + t[i] <= n:
    tp[i + t[i]] = max(tp[i + t[i]], tp[i] + p[i])
    for j in range (i+t[i], n+1):
      tp[j] = max(tp[j], tp[i+t[i]])

print(max(tp))
N = int(input())
ans = []

for i in range (N):
  num = int(input())
  ans.append(num)

ans.sort()
for a in ans:
  print(a)
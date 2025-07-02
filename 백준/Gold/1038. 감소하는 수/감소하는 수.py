n = int(input())
res = []

def dfs(num, ld):
  res.append(num)
  for nd in range (0, ld):
    dfs(num * 10 + nd, nd)

for i in range (10):
  dfs(i, i)

res.sort()

if n >= len(res):
  print(-1)

else:
  print(res[n])
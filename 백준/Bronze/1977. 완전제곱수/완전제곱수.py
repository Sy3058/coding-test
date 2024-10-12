m = int(input())
n = int(input())

psn = [] # perfect square number
i = 1
while i**2 <= n:
  if i**2 >= m:
    psn.append(i**2)
  i += 1

if psn:
  print(sum(psn))
  print(psn[0])
else:
  print(-1)
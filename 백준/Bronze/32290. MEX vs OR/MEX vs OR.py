l, r, x = map(int, input().split())
nl = set()
flag = False

for i in range (l, r + 1):
  nl.add(i | x)

lnl = list(nl)
lnl.sort()

if lnl[0] != 0:
  print(0)

else:
  for i in range (lnl[-1]):
    if i not in nl:
      print(i)
      flag = True
      break

  if not flag:
    print(lnl[-1] + 1)
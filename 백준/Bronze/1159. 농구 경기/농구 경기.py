n = int(input())
possible = dict()

for _ in range (n):
  name = input()
  possible[name[0]] = possible.get(name[0], 0) + 1

ans = []
for f, cnt in possible.items():
  if cnt >= 5:
    ans.append(f)

if ans:
  ans.sort()
  for a in ans:
    print(a, end = '')
else:
  print("PREDAJA")
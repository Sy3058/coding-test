n, m = map(int, input().split())
if n > m:
  a = m
  b = n
else:
  a = n
  b = m

if a == b:
  print(0)
else:
  print(b-a-1)
for i in range (a+1, b):
  if i == b-1:
    print(i)
  else:
    print(i, end= ' ')
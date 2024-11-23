import sys

arr = []
mlen = 0
ans = ''

for _ in range (5):
  row = list(sys.stdin.readline().strip())
  arr.append(row)
  if len(row) > mlen:
    mlen = len(row)

for j in range (mlen):
  for i in range (5):
    if j < len(arr[i]):
      ans += arr[i][j]

print(ans)
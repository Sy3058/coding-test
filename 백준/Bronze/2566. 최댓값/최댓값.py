import sys

mnum = -1
for i in range (9):
  row = list(map(int, sys.stdin.readline().split()))
  if max(row) > mnum:
    mnum = max(row)
    a = i + 1
    b = row.index(mnum) + 1

print(mnum)
print(a, b)
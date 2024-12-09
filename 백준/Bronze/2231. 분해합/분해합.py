import sys

n = int(sys.stdin.readline())
flag = False

for i in range (1, n):
  hap = i
  num = str(i)
  for j in range (len(num)):
    hap += int(num[j])
  
  if n == hap:
    print(i)
    flag = True
    break

if not flag:
  print(0)
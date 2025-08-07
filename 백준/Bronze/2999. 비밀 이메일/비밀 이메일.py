import sys
input = sys.stdin.readline

message = input().strip()
n = len(message)
for i in range (int(n**0.5), 0, -1):
  if n % i == 0:
    r = i # R * C중 가장 큰 R의 값
    break
c = n // r

arr = [[''] * r for _ in range (c)]
for i in range (n):
  arr[i//r][i%r] = message[i]

for i in range (r):
  for j in range (c):
    print(arr[j][i], end = '')
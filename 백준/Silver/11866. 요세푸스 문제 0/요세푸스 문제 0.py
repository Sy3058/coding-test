import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
num = deque([i+1 for i in range (n)])
order = []

while num:
  num.rotate(-k+1)
  order.append(num.popleft())

print('<', end = '')
for i in range (n-1):
  print(order[i], end=', ')
print(order[-1], end = '')
print('>')
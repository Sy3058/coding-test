import sys

n = int(sys.stdin.readline())
x_li = []
y_li = []

for _ in range (n):
  x, y = map(int, sys.stdin.readline().split())
  x_li.append(x)
  y_li.append(y)

x1 = min(x_li)
x2 = max(x_li)
y1 = min(y_li)
y2 = max(y_li)

width = abs(x1 - x2) * abs(y1 - y2)
print(width)
n = int(input())
ops = []

for _ in range (n):
  op = int(input())
  ops.append(op)

c = ops.count(1)
nc = n - c

if c > nc:
  print("Junhee is cute!")
else:
  print("Junhee is not cute!")
k, n, m = map(int, input().split())

total_price = k * n
if total_price > m:
  print(total_price - m)
else:
  print(0)
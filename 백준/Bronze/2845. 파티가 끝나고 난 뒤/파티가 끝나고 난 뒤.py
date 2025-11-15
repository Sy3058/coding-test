l, p = map(int, input().split())
parts = list(map(int, input().split()))

# 1제곱미터당 l명 넓이는 p
people = l * p
for i in parts:
  print(i - people, end = " ")
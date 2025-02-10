import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))
price = oil[0]
total = 0

for i in range (n-1):
  if price > oil[i]:
    price = oil[i]
  total += price*road[i]

print(total)

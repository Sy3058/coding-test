price = 1000 - int(input())
coin = (500, 100, 50, 10, 5, 1)
cnt = 0
for c in coin:
  cnt += price//c
  price %= c

print(cnt)
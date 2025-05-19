T = int(input())

for test_case in range (1, T + 1):
  n = int(input())
  price = list(map(int, input().split()))
  price.reverse()
  profit = 0

  mp = price[0] # max price
  for i in range (1, n):
    if price[i] > mp:
      mp = price[i] # 최대값 변경

    else:
      profit += mp - price[i] # 최대값에서 현재 값 뺀 게 이득

  print("#%d %d"%(test_case, profit))
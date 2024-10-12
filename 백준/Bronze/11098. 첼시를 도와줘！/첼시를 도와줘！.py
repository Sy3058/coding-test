n = int(input()) # number of test case

for _ in range (n):
  p = int(input()) # number of player
  players = {}
  for _ in range (p):
    price, player = input().split()
    players[int(price)] = player
  max_price = max(players.keys())
  print(players[max_price])
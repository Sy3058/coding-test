n = int(input())
for _ in range (n):
  r, e, c = map(int, input().split())
  rp = e - c # real profit
  if r < rp:
    print('advertise')
  elif r > rp:
    print('do not advertise')
  else:
    print('does not matter')
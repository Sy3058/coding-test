n = int(input())
call = list(map(int, input().split()))

def young(call):
  fee = 0
  for i in range (n):
    fee += (call[i]//30 + 1)
  return fee * 10

def minsik(call):
  fee = 0
  for i in range (n):
    fee += (call[i]//60 + 1)
  return fee * 15

y = young(call)
m = minsik(call)

if y > m:
  print('M', m)
elif y < m:
  print('Y', y)
else:
  print('Y M', m)
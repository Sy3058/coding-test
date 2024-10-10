cs, ss = 100, 100 # score of c and s
n = int(input())
for _ in range (n):
  cd, sd = map(int, input().split()) # dice num of c and s
  if cd < sd:
    cs -= sd
  elif cd > sd:
    ss -= cd
print(cs)
print(ss)
def Cantor(N):
  if N == 0:
    return '-'
  return Cantor(N-1) + ' '*(3**(N-1)) + Cantor(N-1)

while True:
  try:
    N = int(input())
    answer = Cantor(N)
    print(answer)
  except EOFError:
    break
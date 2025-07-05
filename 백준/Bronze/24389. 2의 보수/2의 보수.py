n = int(input())
bit = 2**32 - 1 # 32비트
comp = bin((n^bit) + 1)[2:] # XOR을 이용하면 반전시킬 수 있음
bn = bin(n)[2:].zfill(32)
cnt = 0

for i in range (32):
  if comp[i] != bn[i]:
    cnt += 1

print(cnt)
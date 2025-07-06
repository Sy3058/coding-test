import sys
input = sys.stdin.readline

n = int(input())
powers = [1 << i for i in range (61)] # 2^i 리스트

for _ in range (n):
  m = int(input())
  for i in range (61):
    rem = m - powers[i]
    if rem <= 0: # 더이상 검사할 필요 없음
      continue

    if (rem & (rem - 1)) == 0: # rem이 2의 거듭 제곱이면 ex) rem = 1000(2) rem - 1 = 111(2) 이므로 rem & (rem - 1) = 0이 됨
      j = rem.bit_length() - 1
      print(min(i, j), max(i, j))
      break
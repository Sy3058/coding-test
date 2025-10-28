f = [0] * 24
f[1] = 1
f[2] = 2
i = 2
# 피보나치 수열 채우기
while f[i-1] < 25000:
  f[i] = f[i-1] + f[i-2]
  i += 1

for _ in range (int(input())):
  num = int(input())
  bit = []
  for i in range (23, -1, -1):
    if f[i] <= num:
      num -= f[i]
      bit.append(1)
      break
  
  for j in range (i-1, 1, -1):
    if f[j] <= num:
      num -= f[j]
      bit.append(1)
    else:
      bit.append(0)
  bit.pop() # 오른쪽으로 한 비트 시프트 시킨 것과 같은 효과
  ans = 0
  bit.reverse()
  for i in range (len(bit)):
    ans += bit[i] * f[i+2] # bit가 f[2]부터 시작하므로 i에 2를 더해야 원래의 값
  print(ans)
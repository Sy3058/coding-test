import sys

n = int(sys.stdin.readline())

# 에라토스테네스의 체
prime = []
d = 2
d_max = n ** 0.5 # n의 제곱근까지만 확인하면 됨

while d <= d_max:
  if n%d != 0: # 나누어 떨어지지 않을 때
    d += 1 # d 값 증가
  else:
    prime.append(d)
    n //= d # n 값 갱신

if n > 1: # 제곱근까지 나누어떨어지지 않으면 소수
  prime.append(n)

prime_number = list(set(prime))
prime_number_count = []

for i in prime_number:
  cnt = prime.count(i)
  if cnt%2 == 1: # 제곱을 만들어야하므로 모든 인수가 짝수개 있어야함
    cnt += 1
  prime_number_count.append(cnt)

ans = 1
for j in range (len(prime_number)):
  ans *= prime_number[j] ** prime_number_count[j]

print(ans)
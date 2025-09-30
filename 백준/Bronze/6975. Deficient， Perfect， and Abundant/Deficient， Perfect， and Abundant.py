import math

def sum_of(n):
  # 진약수의 합 계산
  proper_sum = 0
  limit = int(math.sqrt(n))

  for i in range (1, limit + 1):
    if n % i == 0:
      # 나누어떨어지면 약수
      proper_sum += i

      # 짝이 되는 약수
      pair = n // i
      if pair != i and pair != n:
        proper_sum += pair
  
  return proper_sum

tc = int(input())
for _ in range (tc):
  n = int(input())
  sn = sum_of(n)
  if sn < n:
    print(f"{n} is a deficient number.\n")
  elif sn == n:
    print(f"{n} is a perfect number.\n")
  else:
    print(f"{n} is an abundant number.\n")
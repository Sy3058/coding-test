import sys
import math

n = int(sys.stdin.readline()) # number of numbers (2~100)
num_list = []

for _ in range (n):
  num = int(sys.stdin.readline()) # number (1~1,000,000,000)
  num_list.append(num)

num_list.sort()

diff_list = []
for i in range (1, n):
  diff = num_list[i] - num_list[i-1]
  diff_list.append(diff)

# 인접한 숫자들 간의 차이의 최대공약수를 구함
gcd_value = diff_list[0]

# 두 수의 차이와 최대 공약수의 최대 공약수를 구함
for i in range (1, n-1):
  gcd_value = math.gcd(gcd_value, diff_list[i])

# 최대공약수의 약수 구하기
result = [gcd_value]
for i in range (2, int(gcd_value ** 0.5)+1): # 문제에서 1은 제외했으므로 2부터 시작
  if gcd_value % i == 0:
    result.append(i)
    if i != gcd_value // i:
      result.append(gcd_value // i)

result.sort()
print(" ".join(map(str, result)))
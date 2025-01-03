import sys
input = sys.stdin.readline

n = 1000000
prime = [True for _ in range (n+1)]

# 에라토스테네스의 체
for i in range (2, int(n**0.5) + 1): # 2부터 n의 제곱근까지의 수를 확인
  if prime[i] == True: # 남은 수인 경우
    # i를 제외한 i의 배수를 False로 변경
    j = 2
    while i * j <= n:
      prime[i * j] = False
      j += 1

def goldbach(num):
  cnt = 0
  for i in range (3, num//2 + 1, 2): # 2를 제외하면 모든 소수가 홀수이므로 홀수만 확인
    if prime[i] == True and prime[num-i] == True:
      cnt += 1
  
  return cnt

t = int(input())
for _ in range (t):
  num = int(input())
  if num == 4: # 4일때만 2가 사용됨 
    print(1)
  else:
    ans = goldbach(num)
    print(ans)
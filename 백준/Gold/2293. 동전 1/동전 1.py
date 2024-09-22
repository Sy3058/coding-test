import sys

n, k = map(int, sys.stdin.readline().split())
values = []
answer = 0

for _ in range (n): # 시간 복잡도 O(n)
  value = int(sys.stdin.readline())
  if value <= 10000: # 가치의 합이 10000 이하이므로 10000을 초과하는 값은 필요하지 않음
    values.append(value)

values.sort() # 시간 복잡도 O(N)

dp = [0] * (k+1) # 사이즈 k+1만큼의 리스트 선언 (0일때는 )
dp[0] = 1 # 인덱스 0은 기본값으로 초기화

for value in values:
  for i in range (value, k+1): # value를 기준으로 갱신 (어차피 value 이하의 값은 갱신되지 않음)
    dp[i] += dp[i-value] # value원을 사용해서 i원을 만들 수 있는 가짓수

print(dp[i])

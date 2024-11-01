import sys

T = int(sys.stdin.readline()) # 테스트케이스

for _ in range (T):
  N = int(sys.stdin.readline()) # 날의 수
  stock = list(map(int, sys.stdin.readline().split())) # 날 별 주가
  cnt = 0
  hap = 0
  profit = 0 # answer
  max_tmp = stock[-1] # 제일 마지막 값이 가장 크다고 가정

  for i in range (N-2, -1, -1): # 뒤에서부터 검사
    if stock[i] < max_tmp: # 앞의 값이 더 작다면
      cnt += 1
      hap += stock[i]
    else: # 뒤의 값이 크거나 같다면 (== 이익이 생길때)
      profit += max_tmp*cnt - hap
      cnt = 0
      hap = 0
      max_tmp = stock[i]
      
  profit += max_tmp*cnt - hap
  
  print(profit)
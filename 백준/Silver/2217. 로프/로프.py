import sys
input = sys.stdin.readline

n = int(input())
weight = [int(input()) for _ in range (n)]

weight.sort(reverse = True) # 큰 무게부터 정렬
mw = 0 # 최대로 버틸 수 있는 중량

for i in range (n):
  k = i+1 # 로프의 개수
  w = k * weight[i] # 하나의 로프가 버틸 수 있는 최소 중량 * k == k개의 로프가 버틸 수 있는 최대 중량
  mw = max(w, mw)

print(mw)
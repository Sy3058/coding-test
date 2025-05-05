import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range (n)]
houses.sort()

def binary_search(houses, s, e):
  while s <= e:
    mid = (s + e) // 2 # 최소 거리와 최대 거리의 중간값
    cur = houses[0] # 현재 공유기가 설치되어 있는 위치
    cnt = 1

    for i in range (1, n):
      if houses[i] >= cur + mid: # 중간값보다 i번째 집과 첫번째 집의 거리 차가 커지면 i번째 집에 공유기 설치
        cnt += 1
        cur = houses[i] # 현재 공유기가 설치되어 있는 집
    
    if cnt >= c:
      global answer
      s = mid + 1
      answer = mid
    
    else:
      e = mid - 1

s = 1 # 최소 거리는 1
e = houses[-1] - houses[0] # 제일 끝에 있는 집과 처음에 있는 집 사이의 거리가 최대 거리
answer = 0

binary_search(houses, s, e)
print(answer)
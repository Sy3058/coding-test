import heapq
import sys
input = sys.stdin.readline

# heap은 첫번째 값이 가장 작다는 것만 보장함
for tc in range (1, int(input()) + 1):
  k = int(input())
  maxh = [] # 최대힙
  minh = [] # 최소힙
  # 숫자의 존재 여부와 개수를 관리하는 딕셔너리
  num_cnt = dict()

  for _ in range (k):
    command, n = input().split()
    n = int(n)

    if command == "I": # 넣기
      heapq.heappush(minh, n)
      heapq.heappush(maxh, -n)
      num_cnt[n] = num_cnt.get(n, 0) + 1 # 딕셔너리에 숫자 개수 갱신
    
    else:
      if not minh: # 힙이 비어있으면 무시
        continue
    
      if n == 1: # 최댓값 삭제
        while maxh: # 없으면 해당하는 수가 나올 때까지 계속 pop
          value = -heapq.heappop(maxh)
          if num_cnt.get(value, 0) > 0:
            num_cnt[value] -= 1
            break
      
      else: # 최솟값 삭제
        while minh:
          value = heapq.heappop(minh)
          if num_cnt.get(value, 0) > 0:
            num_cnt[value] -= 1
            break

  # 유효한 최댓값 찾기
  # while문이 끝나고 minh에 남은 첫번째 값이 최댓값
  while minh and num_cnt.get(minh[0], 0) == 0:
    heapq.heappop(minh)
  
  # 유효한 최솟값 찾기
  while maxh and num_cnt.get(-maxh[0], 0) == 0:
    heapq.heappop(maxh)
  
  if not minh:
    print("EMPTY")
  else:
    print(-maxh[0], minh[0])
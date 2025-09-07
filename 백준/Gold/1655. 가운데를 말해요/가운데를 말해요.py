import heapq
import sys
input = sys.stdin.readline

def sol():
  n = int(input())
  left = [] # 최대 힙
  right = [] # 최소 힙
  
  for i in range (n):
    num = int(input())

    # 최대 힙에 값 넣기
    if not left or num <= -left[0]:
      heapq.heappush(left, -num) # 최대 힙을 따로 제공하지 않으므로 -값을 넣어서 최대 힙으로 유지
    else:
      heapq.heappush(right, num) # 오른쪽을 오름차순으로 유지
    
    # 균형 맞추기 (항상 왼쪽의 개수가 오른쪽의 개수 or +1)
    if len(left) > len(right) + 1:
      heapq.heappush(right, -heapq.heappop(left))
    elif len(left) < len(right):
      heapq.heappush(left, -heapq.heappop(right))
    
    # 중간값은 항상 left에서 가장 큰 값
    print(-left[0])
    
sol()
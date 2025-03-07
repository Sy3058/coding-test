import sys
import heapq
input = sys.stdin.readline

n = int(input())
c = [tuple(map(int, input().split())) for _ in range (n)] # 수업

c.sort(key = lambda x:(x[0], x[1])) # 시작 시간 빠른 순으로 정렬 (같으면 끝나는 시간 빠른 순)

cr = [] # 강의실에 끝나는 시간을 저장장
heapq.heappush(cr, c[0][1])

for i in range (1, n):
  if c[i][0] < cr[0]: # 시작 시간이 가장 빠른 끝나는 시간보다도 작다면 강의실이 더 필요
    heapq.heappush(cr, c[i][1])
  else: # 가장 빨리 끝난 강의에 다음 강의 배정
    heapq.heappop(cr)
    heapq.heappush(cr, c[i][1])

print(len(cr))
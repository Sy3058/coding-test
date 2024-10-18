import sys
from collections import deque

# N: 접시의 수, d: 초밥의 가짓수, k: 연속해서 먹는 접시의 수, c: 쿠폰 번호
N, d, k, c = map(int, sys.stdin.readline().split())
rails = [] # 레일에 놓인 초밥
ans = 0
tmp = 0 # 임시로 최댓값 확인

for _ in range (N):
  r = int(sys.stdin.readline())
  rails.append(r)

sort = list(set(rails)) # 레일 위에 있는 초밥 종류 리스트
snum = len(sort) # 총 가짓수
case = deque(rails[:k]) # k개 연속해서 먹었을 때 먹은 초밥
rest = deque(rails[k:]) # 나머지 초밥

for _ in range (N):
  usort = set(case) # case에 존재하는 초밥의 종류
  if len(usort) == k: # 정답이 최대일 때
    if c in usort: # 쿠폰에 해당하는 초밥이 있다면
      tmp = k # 최대는 아님
    else:
      ans = k+1 # 이때가 최대이므로 멈춤
      break
  else:
    if c in usort:
      if tmp < len(usort): # 기존의 최댓값보다 새로운 값이 크다면 기존의 최댓값 업데이트
        tmp = len(usort)
    else:
      if tmp < len(usort)+1:
        tmp = len(usort)+1
  # case의 초밥을 회전시킴
  rest.append(case.popleft())
  case.append(rest.popleft())

if ans != 0:
  print(ans)
else:
  print(tmp)
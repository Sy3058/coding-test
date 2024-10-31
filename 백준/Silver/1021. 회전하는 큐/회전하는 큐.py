from collections import deque

N, M = map(int, input().split()) # 큐의 크기, 뽑아내려고 하는 수의 개수
num_list = deque([i for i in range (N)]) # 큐
p_list = list(map(int, input().split())) # 뽑아내려고 하는 수의 위치
cnt = 0 # 2번과 3번 연산의 수

for i in range (M):
  p = p_list[i] - 1 # 인덱스는 0부터 시작하므로 -1
  if p == num_list[0]: # 바로 뽑을 수 있는 경우
    num_list.popleft()
  else:
    if num_list.index(p) < len(num_list) / 2: # 왼쪽으로 이동시키는 게 최소
      while num_list[0] != p: # num_list[0] == p가 되면 break
        tmp = num_list.popleft()
        num_list.append(tmp) # 2번 
        cnt += 1
      num_list.popleft() # num_list[0] == p이므로
    else:
      while num_list[0] != p:
        tmp = num_list.pop()
        num_list.appendleft(tmp) # 3번
        cnt += 1
      num_list.popleft()

print(cnt)
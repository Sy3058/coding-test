import sys
input = sys.stdin.readline

# 정방향 연산과 역방향 연산시 갈 수 있는 위치 미리 찾아두기
L = 10000 # 가능한 수

path_for = [] # 정방향 연산의 결과
path_rev = [] # 역방향 연산의 결과

for i in range (L):
  d1 = i//1000
  d2 = (i % 1000) // 100
  d3 = (i % 100) // 10
  d4 = (i % 10)
  
  di = (i * 2) % 10000
  si = 9999 if i == 0 else i-1 # i = 0이면 i-1은 9999
  li = ((d2 * 10 + d3) * 10 + d4) * 10 + d1 # 1234 -> 2341
  ri = ((d4 * 10 + d1) * 10 + d2) * 10 + d3 # 1234 -> 4123

  # path_rev에서 D의 값이 두개가 되므로 추후 연산을 편하게 하려면 D가 마지막에 들어가야됨
  path_for.append((si, li, ri, di))

  sirev = 0 if i == 9999 else i+1
  if i % 2 == 0: # 짝수일 때만 d의 역연산이 존재
    direv1 = i // 2
    # 이때 direv는 i//2와 i//2 + 5000 (i * 2가 10000 이상일 때) 두 가지 존재
    direv2 = i // 2 + 5000
    path_rev.append((sirev, ri, li, direv1, direv2)) # li와 ri는 역연산일 때 반대로 작용
  else:
    # 홀수일 때는 d의 역연산이 없으므로 넣지 않음
    path_rev.append((sirev, ri, li))

for tc in range (int(input())):
  a, b = map(int, input().split())

  dp = [0] * L

  def bfs():
    dp[a] = 1
    dp[b] = -1 # 역연산은 음수로 확인
    nv_for = [a] # 정방향 큐
    nv_rev = [b] # 역방향 큐

    # 정방향은 2부터 4999까지 확인 (a로부터의 거리)
    # 역방향은 -2부터 -4999까지 확인 (b로부터의 거리)
    # 단방향으로 최대 10000번의 연산이 필요하므로 역연산은 그 반만 확인하면 됨
    for i, j in zip(range(2, 5000), range(-2, -5000, -1)):
      new_for = [] # 정방향의 다음 레벨을 저장할 임시 큐
      for nv in nv_for: # 현재 큐에 있는 모든 수를 확인
        for k in path_for[nv]: # path_for를 이용해서 그 수가 갈 수 있는 모든 방향을 확인
          if not dp[k]: # 방문한 적 없을 때만 방문
            dp[k] = i
            new_for.append(k)
          
          elif dp[k] < 0: # 역방향으로 방문한 적 있다면 두 BFS가 만난 것
            # 정방향 탐색 단계에서 발견됐으므로 현재 역방향이 아니라 이전 역방향에서 이미 여기 도착한 것 따라서 역방향의 실제 거리는 j+1이 아니고 그 이전인 j+2
            return i-1, j+2, k # 정방향의 실제 거리, 역방향의 실제 거리, 만난 노드
      
      nv_for = new_for # 임시 큐로 바꿔주기
      
      new_rev = [] # 역방향의 다음 레벨을 저장할 임시 큐
      for nv in nv_rev:
        for k in path_rev[nv]:
          if not dp[k]:
            dp[k] = j
            new_rev.append(k)
          
          elif dp[k] > 0:
            return i-1, j+1, k
      
      nv_rev = new_rev
  
  i, j, k = bfs() # 정방향 거리, 역방향 거리, 만난 노드

  # 경로 역추적
  answer = [None] * (i-j) # j가 음수이므로 -를 해줘야 실제 거리가 됨

  # 정방향 역추적
  cur = k
  for cur_dis in range (i, 0, -1): # 정방향이었으므로 역순으로 추적
    for command, before in zip(('S', 'L', 'R', 'D', 'D'), path_rev[cur]): # 역방향의 경우 가능한 방향이 S L R D D로 총 5개였음을 기억하기
      if dp[before] == cur_dis: # 이전 노드인 before의 값이 현재 거리인 cur_dis와 같으면 answer[cur_dis-1]에 해당하는 명령어가 command
        answer[cur_dis-1] = command
        cur = before # 현재값 갱신
        break
  
  # 역방향 추적
  cur = k
  for cur_dis in range (j, 0): # 역방향이었으므로 순서대로 추적
    for command, nxt in zip(('S', 'L', 'R', 'D'), path_for[cur]):
      if dp[nxt] == cur_dis:
        answer[cur_dis] = command # 순서대로 추적하고 있으므로 cur_dis에 해당하는 명령어가 command
        cur = nxt
        break

  print(''.join(answer))



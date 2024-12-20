import sys

T = int(sys.stdin.readline()) # 테스트 데이터의 수

for _ in range (T):
  n, k, t, m = map(int, sys.stdin.readline().split()) # 팀의 개수, 문제의 개수, 팀의 ID, 로그 엔트리의 개수
  log = [[] for _ in range (n+1)]
  scores = [0]
  last = [0]
  trial = [0]

  for o in range (m): # 로그
    i, j, s = map(int, sys.stdin.readline().split()) # 팀 ID, 문제 번호, 획득한 점수
    log[i].append((j,s,o)) # o는 로그 순서
  
  for team in range (1, n+1):
    last.append(log[team][-1][2]) # 해당 팀의 마지막 제출
    trial.append(len(log[team])) # 해당 팀의 제출 횟수수
    log[team].sort(key = lambda x:x[1], reverse = True) # 점수가 높은 순으로 정렬
    log[team].sort(key = lambda x:x[0]) # 문제 번호 순으로 정렬

    score = log[team][0][1]
    for num in range (1, len(log[team])):
      if log[team][num][0] != log[team][num-1][0]: # 점수 높은 순으로 정렬했으므로 번호가 바뀌는 순간의 점수가 해당 번호 점수 중 가장 높은 점수
        score += log[team][num][1]
    scores.append(score)
  
  team_score = scores[t]
  rank = 1
  for a in range (1, n+1):
    if scores[a] > team_score:
      rank += 1
    
    elif a!= t and scores[a] == team_score:
      if trial[a] < trial[t]: # 해당 팀보다 더 적게 시도했다면
        rank += 1
      elif trial[a] == trial[t]:
        if last[a] < last[t]: # 해당 팀보다 더 빨리 제출했다면
          rank += 1

  print(rank)

import sys

T = int(sys.stdin.readline()) # test case

for _ in range (T):
  N = int(sys.stdin.readline())
  ranking = list(map(int, sys.stdin.readline().split()))
  ans_score = 0
  ans = 0

  team_list = set(ranking)
  team_score = {team: [] for team in team_list} # team_list를 key로 value가 모두 []인 딕셔너리 생성
  cnt = {team: 0 for team in team_list} # value가 모두 0인 딕셔너리 생성
  score = 1

  for i in ranking:
    cnt[i] += 1
  
  for i in range (N):
    if cnt[ranking[i]] == 6:
      team_score[ranking[i]].append(score)
      score += 1 # 6명이 되지 않는 팀은 점수에서 제외
    
    if len(team_score[ranking[i]]) == 5:
      tmp = sum(team_score[ranking[i]][:4]) # 4명까지의 점수만 더함
      if ans_score == 0 or tmp < ans_score:
        ans = ranking[i]
        ans_score = tmp

  print(ans)
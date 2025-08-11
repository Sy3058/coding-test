import sys
input = sys.stdin.readline

def play_game(batting_order, inning_data, n):
  total_score = 0
  batter_idx = 0 # 시작 선수
  for inning in range(n):
    out_count = 0
    b1, b2, b3 = 0, 0, 0

    while out_count < 3:
      player_number = batting_order[batter_idx]
      result = inning_data[inning][player_number - 1] # 인덱스가 0부터 시작하므로 1 빼야 함

      # out
      if result == 0:
        out_count += 1
      
      # 1루타
      elif result == 1:
        total_score += b3
        b1, b2, b3 = 1, b1, b2
      
      # 2루타
      elif result == 2:
        total_score += (b2 + b3)
        b1, b2, b3 = 0, 1, b1

      # 3루타
      elif result == 3:
        total_score += (b1 + b2 + b3)
        b1, b2, b3 = 0, 0, 1
      
      # 홈런
      else:
        total_score += (b1 + b2 + b3 + 1)
        b1, b2, b3 = 0, 0, 0
      
      batter_idx = (batter_idx + 1) % 9
  return total_score

n = int(input())
inning_results = [list(map(int, input().split())) for _ in range (n)]

possible_batting_order = (0, 1, 2, 4, 5, 6, 7, 8) # 4번 타자를 제외하고 정할 수 있음
batting_order = [0, 0, 0, 1, 0, 0, 0, 0, 0]
picked = [True] * 2 + [False] * 8
max_score = 0

def backtrack(idx, batting_order):
  global max_score
  if idx == 8:
    cur_score = play_game(batting_order, inning_results, n)
    if cur_score > max_score:
      max_score = cur_score
    return
  
  for i in range (2, 10): # 넣을 수 있는 선수들
    if picked[i]:
      continue
    batting_order[possible_batting_order[idx]] = i
    picked[i] = True
    backtrack(idx+1, batting_order)
    picked[i] = False
    batting_order[possible_batting_order[idx]] = 0 # 초기화

backtrack(0, batting_order)
print(max_score)
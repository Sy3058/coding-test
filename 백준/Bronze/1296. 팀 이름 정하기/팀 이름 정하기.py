import sys
input = sys.stdin.readline

def calculate(y, t):
  # 어차피 연두와 팀 이름에서 등장하는 개수를 모두 더하므로 그냥 둘을 더한 새로운 string 생성
  s = y + t
  L = s.count("L")
  O = s.count("O")
  V = s.count("V")
  E = s.count("E")
  score = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
  return score

yeondu = input().strip()
top_score = -1
winner = '' # 승리할 팀
n = int(input()) # 팀 이름 후보의 개수
for _ in range (n):
  name = input().strip()
  score = calculate(yeondu, name)
  if score > top_score:
    winner = name
    top_score = score
  
  elif score == top_score:
    # 점수가 동일한 경우 사전 순으로 가장 앞서는 팀
    winner = sorted([winner, name])[0]

print(winner)
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 총 걸그룹 수, 맞혀야 할 문제의 수
groups = dict()
# n개의 걸그룹 저장
for _ in range (n):
  team_name = input().strip() # 팀 이름을 키로 저장
  groups[team_name] = []
  for i in range (int(input())):
    groups[team_name].append(input().strip())
  groups[team_name].sort()

# m개의 줄에 퀴즈를 입력 받음
for _ in range (m):
  question = input().strip()
  option = int(input())

  if option == 0: # 0이면 팀이름
    for member in groups[question]:
      print(member)
  
  else: # 1이면 멤버의 이름
    for group, members in groups.items():
      if question in members:
        print(group)
        break
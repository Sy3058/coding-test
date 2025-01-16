import sys
input = sys.stdin.readline

n, type = input().strip().split()
n = int(n)
player = set()

for _ in range (n):
  player.add(input().strip()) # set을 이용해서 중복 제거

# 필요 인원수 - 1이 실제로 필요한 명수; 최대 플레이 횟수이므로 명수//실제 필요한 명수가 답
if type == 'Y':
  print(len(player))
elif type == 'F':
  print(len(player)//2)
else:
  print(len(player)//3)

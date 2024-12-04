import sys

p, m = map(int, sys.stdin.readline().split()) # 플레이어의 수, 방의 정원
l, n = sys.stdin.readline().split()
l = int(l)

rooms = [[(l, n)]]

for _ in range (p-1):
  l, n = sys.stdin.readline().split()
  l = int(l)
  flag = False # 방에 입장했는지 확인

  for i in range (len(rooms)):
    lv = rooms[i][0][0] # 기준이 되는 레벨
    if len(rooms[i]) < m and lv-10 <= l <= lv+10: # 정원이 차지 않았고 기준 레벨 -10부터 +10 사이일 때
      rooms[i].append((l, n))
      flag = True # 방에 입장
      break
  
  if not flag: # 기존의 room을 다 돌았는데 방에 입장하지 못한 경우
    rooms.append([(l, n)])

for i in range (len(rooms)):
  rooms[i].sort(key = lambda x: x[1]) # 이름을 기준으로 정렬
  if len(rooms[i]) == m:
    print('Started!')
    for j in range (m):
      print(rooms[i][j][0], rooms[i][j][1])
  
  else:
    print('Waiting!')
    for k in range (len(rooms[i])):
      print(rooms[i][k][0], rooms[i][k][1])
import sys
input = sys.stdin.readline

n = int(input())
arr = []
t = 0 # 선생님 명수
for _ in range (n):
  row = list(input().strip().split())
  t += row.count('T')
  arr.append(row)

directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

def check_S(x, y): # 학생을 감시할 수 있는지 확인하는 함수
  for dx, dy in directions:
    nx, ny = x + dx, y + dy

    while 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 'O': # 장애물과 만나거나 범위에서 벗어나면 탐색 종료
      if arr[nx][ny] == 'S':
        return True # 감시 가능
      else: # 다음 방향 탐색
        nx += dx
        ny += dy
    
  return False

def solution(cnt):
  global answer
  if cnt == 3: # 장애물 개수가 3개가 되면
    tcnt = 0 # 선생님 수
    for i in range (n):
      for j in range (n):
        if arr[i][j] == 'T':
          if not check_S(i, j): # 감시할 수 있는 학생이 없는 경우
            tcnt += 1
    if tcnt == t: # 모든 선생님이 감시가 불가능할 때
      answer = True
    return
  
  for i in range (n):
    for j in range (n):
      if arr[i][j] == 'X':
        arr[i][j] = 'O'
        cnt += 1
        solution(cnt)
        arr[i][j] = 'X' # 설치했던 장애물 제거
        cnt -= 1

answer = False
solution(0)
if answer:
  print('YES')
else:
  print('NO')

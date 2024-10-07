import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[0] * n for _ in range (n)] # node의 개수만큼 array 생성 (이때 node1의 인덱스는 0임)

for _ in range (m):
  a, b = map(int, sys.stdin.readline().split())
  arr[a-1][b-1] = 1 # 연결된 node를 1로 표시
  arr[b-1][a-1] = 1

def search(start, arr):
  visited = []
  need_visited = [start]

  while need_visited: # 방문 예정지가 있는 동안
    temp = need_visited.pop()
    visited.append(temp)
    for i in range (n):
      if arr[temp][i] == 1: # 연결되어 있는 경우
        if i not in visited and i not in need_visited:
          need_visited.append(i) # 방문된 적 없고 방문 예정에도 없으면 방문 예정에 추가
  return visited

checked = [] # 확인된 번호

visited = search(0, arr) 
checked.extend(visited)
count = 1

idx = 1
while idx != n:
  if idx not in checked and 1 in arr[idx]: # 검사된 적 없고 연결된 노드가 존재하는 경우
    visited = search(idx, arr)
    checked.extend(visited)
    count += 1
  elif 1 not in arr[idx]: # 노드가 존재하지만 어느곳과도 연결되지 않은 경우
    checked.append(idx)
    count += 1 

  if len(checked) == n:
    break
  idx += 1

print(count)
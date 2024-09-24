import sys

num = int(sys.stdin.readline()) # 컴퓨터의 수
n = int(sys.stdin.readline()) # 직접 연결되어 있는 컴퓨터 쌍의 수

arr = [[0] * num for _ in range(num)]

for _ in range (n):
  a, b = map(int,sys.stdin.readline().split())
  arr[a-1][b-1] = 1
  arr[b-1][a-1] = 1

def virus(arr, start_node):
  need_visited = [start_node] # 이때 start_node는 1이 아니고 0임
  visited = []

  while need_visited:
    temp = need_visited.pop() # 검사할 숫자를 temp로 지정
    if temp not in visited: # temp에 해당하는 숫자가 방문된 적 없다면
      visited.append(temp) # visited에 temp 추가
      for i in range (len(arr)): # temp와 연결된 컴퓨터 확인
        if arr[temp][i] == 1 and i not in need_visited and i not in visited: # 연결된 컴퓨터 중 방문 예정도, 방문된 적도 없는 컴퓨터를 찾음
          need_visited.append(i) # 만약 있다면 방문 예정에 추가
  return len(visited)-1 # 1번 컴퓨터는 제외해야하므로

answer = virus(arr, 0)

print(answer)

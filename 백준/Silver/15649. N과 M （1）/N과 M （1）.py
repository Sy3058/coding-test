n, m = map(int, input().split())

arr = [] # 출력할 숫자 저장
visited = [False] * (n+1) # 방문되었는지 확인 (인덱스가 0부터 시작하므로 n+1까지)

def dfs():
  if len(arr) == m: # 수열의 크기는 m
    print(' '.join(map(str, arr)))
    return
  
  for i in range (1, n+1):
    if visited[i]:
      continue # 방문된 적 있다면 아래를 진행하지 않음
    visited[i] = True
    arr.append(i)
    dfs() # 재귀함수. 수열의 크기를 만족했다면 그 값이 print됨
    arr.pop()
    visited[i] = False

dfs()
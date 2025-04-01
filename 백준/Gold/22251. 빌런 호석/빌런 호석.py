import sys
input = sys.stdin.readline

n, k, p, x = map(int, input().split())

board = [[0,4,3,3,4,3,2,3,1,2], [4,0,5,3,2,5,6,1,5,4], [3,5,0,2,5,4,3,4,2,3], [3,3,2,0,3,2,3,2,2,1], [4,2,5,3,0,3,4,3,3,2], [3,5,4,2,3,0,1,4,2,1], [2,6,3,3,4,1,0,5,1,2], [3,1,4,2,3,4,5,0,4,3], [1,5,2,2,3,2,1,4,0,1], [2,4,3,1,2,1,2,3,1,0]] # board[a][b] : a -> b로 바꿀 때 반전시켜야 하는 LED의 개수
cnt = 0

fn, fx = str(n).zfill(k), str(x).zfill(k) # 만약 k의 개수보다 n과 x의 자리수가 작다면 앞에 0을 채워줌

def dfs(dep, cnt, fx): # 깊이, 남은 반전 가능 횟수, 현재 층
  if dep >= len(fx):
    if 1 <= int(fx) <= n and int(fx) != x: # 1~n층 사이이고 자기 자신이 아닐 때
      return 1
    
    else:
      return 0
  
  ans = 0
  cur = int(fx[dep]) # 바꿀 숫자

  for i in range (10):
    if cur == i: # 동일한 숫자면 반전되지 않으므로 깊이만 증가
      ans += dfs(dep+1, cnt, fx)

    elif board[cur][i] <= cnt: # 남은 반전 가능 횟수보다 필요한 반전 횟수가 작아야 함
      nx = fx[:dep] + str(i) + fx[dep+1:] # next x
      ans += dfs(dep+1, cnt - board[cur][i], nx)
    
  return ans

print(dfs(0, p, fx))
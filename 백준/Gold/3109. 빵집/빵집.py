import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range (r)]
visited = [[False] * c for _ in range (r)]
deltas = ((-1, 1), (0, 1), (1, 1)) # 위 가운데 아래 순서
cnt = 0

def dfs(x, y):
    visited[x][y] = True
    if y == c - 1:
        return True  # 성공적으로 파이프 연결 완료

    for dx, dy in deltas:
        nx, ny = x + dx, y + dy

        if 0 <= nx < r and 0 <= ny < c:
            if not visited[nx][ny] and board[nx][ny] == '.':
                if dfs(nx, ny):  # 재귀 DFS
                    return True  # 성공한 경로는 더 탐색하지 않음

    return False  # 실패한 경로

for i in range (r):
  if dfs(i, 0): # 성공한 경로라면
    cnt += 1

print(cnt)
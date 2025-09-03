import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

horses = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))

# visited[row][col][남은 horse jump]
visited = [[[False] * (k + 1) for _ in range(w)] for _ in range(h)]

def bfs():
    q = deque([(0, 0, k, 0)]) # x, y, 남은 horse jump, 이동 횟수
    visited[0][0][k] = True

    while q:
        cx, cy, cki, moves = q.popleft()

        # 타겟에 도착했을 때 이동에 걸린 횟수 리턴
        if cx == h - 1 and cy == w - 1:
            return moves

        # 한 칸씩 이동
        for dx, dy in deltas:
            nx, ny = cx + dx, cy + dy
            # 범위와 방문 여부 확인
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 0 and not visited[nx][ny][cki]:
                visited[nx][ny][cki] = True
                q.append((nx, ny, cki, moves + 1))

        # k > 0일 때 말의 움직임
        if cki > 0:
            for dx, dy in horses:
                nx, ny = cx + dx, cy + dy
                # 범위와 방문 여부 확인
                if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == 0 and not visited[nx][ny][cki - 1]:
                    visited[nx][ny][cki - 1] = True
                    q.append((nx, ny, cki - 1, moves + 1))

    return -1 # 타겟에 도착할 수 없을 때

result = bfs()
print(result)
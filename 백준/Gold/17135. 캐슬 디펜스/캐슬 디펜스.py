import sys
from collections import deque
input = sys.stdin.readline

# 거리가 d 이하인 적 중 가장 가까운 적
def bfs(x, y, length):
    q = deque()
    q.append((x, y, length))
    visited = [[0 for _ in range(m)] for _ in range(n+1)]  # 궁수 위치 포함
    visited[x][y] = 1
    attack = []

    while q:
        x, y, length = q.popleft()

        # 그래프의 해당 위치에 적이 있고 공격가능 거리 안에 있을 때
        if temp[x][y] == 1 and length <= d:
            attack.append((length, y, x))  # (거리, 열, 행)
            continue

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문 조건 반드시 체크
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and length + 1 <= d:
                visited[nx][ny] = 1
                q.append((nx, ny, length + 1))

    return sorted(attack)

# 적을 이동시키기
def graph_move():
    for i in range(n - 1, 0, -1):
        for j in range(m):
            temp[i][j] = temp[i-1][j]
    for j in range(m):
        temp[0][j] = 0

# 적의 존재 여부 (while문 종료 조건)
def is_empty():
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 1:
                return False
    return True

# 조합 구현
def combinations(array, r):
    result = []
    for i in range(len(array)):
        if r == 1:
            result.append([array[i]])
        else:
            for next in combinations(array[i+1:], r-1):
                result.append([array[i]] + next)
    return result

n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] + [[-1] * m]

# 궁수 입장에서 탐색하므로 위로만 탐색하면 됨
dx = [-1, 0, 0]
dy = [0, -1, 1]

items = [i for i in range(m)]
result = 0

for a in combinations(items, 3):
    # deepcopy 대신 슬라이싱 복사
    temp = [row[:] for row in graph]
    cnt = 0

    while not is_empty():
        position = []  # 적 좌표
        for i in range(3):
            target_enemy = bfs(n, a[i], 0)
            if target_enemy:
                target_enemy = target_enemy[0]
                position.append((target_enemy[2], target_enemy[1]))
        
        # 중복 제거
        position = list(set(position))

        for x, y in position:
            temp[x][y] = 0
            cnt += 1

        graph_move()

    result = max(result, cnt)

print(result)
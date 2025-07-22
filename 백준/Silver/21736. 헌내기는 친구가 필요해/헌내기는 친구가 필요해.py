import sys
input = sys.stdin.readline

n, m = map(int, input().split())
campus = []
for i in range (n):
    campus.append(list(input().strip()))
    for j in range (m):
        if campus[i][j] == 'I':
            s = (i, j)

deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))
v = [[False] * m for _ in range (n)]
def dfs(s):
    nv = [s]
    cnt = 0

    while nv:
        x, y = nv.pop()
        v[x][y] = True

        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and campus[nx][ny] != 'X':
                if campus[nx][ny] == 'P':
                    cnt += 1
                v[nx][ny] = True
                nv.append((nx, ny))
    return cnt

cnt = dfs(s)
if cnt == 0:
    print('TT')
else:
    print(cnt)
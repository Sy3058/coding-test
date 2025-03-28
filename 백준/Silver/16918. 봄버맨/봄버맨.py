import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

if n <= 1:  # 초기 상태 출력
    for row in board:
        print(''.join(row))

elif n % 2 == 0:  # 모든 칸에 폭탄이 있는 상태 출력
    for _ in range(r):
        print('O' * c)

else:
    # 첫 번째 폭발 이후 상태 계산
    e1 = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                e1[i][j] = '.'
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c:
                        e1[ni][nj] = '.'

    # 두 번째 폭발 이후 상태 계산
    e2 = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if e1[i][j] == 'O':
                e2[i][j] = '.'
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < r and 0 <= nj < c:
                        e2[ni][nj] = '.'

    # 시간 n에 따른 출력
    if n % 4 == 3:
        for row in e1:
            print(''.join(row))
    elif n % 4 == 1:
        for row in e2:
            print(''.join(row))
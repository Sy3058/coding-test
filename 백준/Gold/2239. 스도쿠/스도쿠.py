import sys
input = sys.stdin.readline

board = []
blank = []

for i in range(9):
    s = input().strip()
    row = []
    for j in range(9):
        c = int(s[j])
        row.append(c)
        if c == 0:
            blank.append((i, j))
    board.append(row)

def check(x, y, num):
    for i in range(9):
        if board[x][i] == num:  # 행 검사
            return False
        if board[i][y] == num:  # 열 검사
            return False

    # 3x3 블록 검사
    start_x = 3 * (x // 3)
    start_y = 3 * (y // 3)
    for i in range(start_x, start_x + 3):
        for j in range(start_y, start_y + 3):
            if board[i][j] == num:
                return False

    return True

def fill(idx):
    if idx == len(blank):
        for i in range(9):
            print(''.join(map(str, board[i])))
        return True  # 정답을 찾았으면 True 반환

    x, y = blank[idx]
    for num in range(1, 10):
        if check(x, y, num):
            board[x][y] = num
            if fill(idx + 1):  # 다음 칸으로 진행
                return True  # 정답을 찾았으면 상위로 계속 True 반환
            board[x][y] = 0  # 백트래킹

    return False  # 어떤 숫자도 안 되면 False 반환

fill(0)

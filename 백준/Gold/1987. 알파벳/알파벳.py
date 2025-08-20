import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
deltas = [(1,0),(0,1),(-1,0),(0,-1)]
answer = 0

# 메모이제이션: 방문한 (x,y,bitmask) 상태 기록
visited_state = dict()

def dfs(x, y, bitmask, depth):
    global answer
    
    # 최대 길이 갱신
    if depth > answer:
        answer = depth
    
    # 가지치기: 남은 최대 알파벳 수로 answer를 넘길 수 없는 경우 종료
    max_remain = 26 - bin(bitmask).count('1')
    if depth + max_remain <= answer:
        return
    
    # 중복 상태 방지
    state_key = (x, y, bitmask)
    if state_key in visited_state:
        return
    visited_state[state_key] = True
    
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            ch_bit = 1 << (ord(board[nx][ny]) - ord('A'))
            if not (bitmask & ch_bit):
                dfs(nx, ny, bitmask | ch_bit, depth + 1)

start_bit = 1 << (ord(board[0][0]) - ord('A'))
dfs(0, 0, start_bit, 1)
print(answer)

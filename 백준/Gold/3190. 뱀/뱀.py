import sys
from collections import deque
input = sys.stdin.readline

n = int(input())  # 보드 크기
k = int(input())  # 사과 개수
apple = set(tuple(map(int, input().split())) for _ in range(k))  # 사과 위치
l = int(input())  # 방향 변환 개수
red = {int(x): c for x, c in (input().split() for _ in range(l))}  # 방향 변환을 dict 형태로 저장

# 방향 벡터 (시계 방향)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0  # 초기 방향 (오른쪽)
snake = deque([(1, 1)])  # 뱀의 위치
snake_positions = set(snake)  # 현재 뱀의 몸 위치를 set으로 관리
cnt = 0  # 시간

while True:
    cnt += 1
    x, y = snake[-1]
    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy

    # 벽에 부딪히거나 자기 자신과 부딪히면 종료
    if not (1 <= nx <= n and 1 <= ny <= n) or (nx, ny) in snake_positions:
        break

    # 이동
    snake.append((nx, ny))
    snake_positions.add((nx, ny))

    # 사과가 없으면 꼬리 제거
    if (nx, ny) not in apple:
        tail_x, tail_y = snake.popleft()
        snake_positions.remove((tail_x, tail_y))
    else:
        apple.remove((nx, ny))  # 사과 제거

    # 방향 변환
    if cnt in red:
        if red[cnt] == 'L':  # 반시계 방향 회전
            direction = (direction - 1) % 4
        else:  # 시계 방향 회전
            direction = (direction + 1) % 4

print(cnt)
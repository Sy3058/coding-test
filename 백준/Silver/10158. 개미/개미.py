"""

x축과 y축이 독립적으로 움직인다고 생각하기

-> 실질적으로 x축 이동은 t % 2w, y축 이동은 t % 2h

"""

w, h = map(int, input().split())

p, q = map(int, input().split())

t = int(input())

# X 좌표 계산

nx = (p + t) % (2 * w)

if nx > w:

    nx = 2 * w - nx

# Y 좌표 계산

ny = (q + t) % (2 * h)

if ny > h:

    ny = 2 * h - ny

print(nx, ny)


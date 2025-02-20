x, y, w, s = map(int, input().split())
if x < y: x, y = y, x

if w > s: # 무조건 대각선으로 가는 게 이득인 경우
  time = s*(x-(x-y)%2) + w*((x-y)%2)
elif 2*w > s: # 일직선은 일직선으로, 대각선은 대각선으로 가는 게 이득인 경우
  time = s*y + w*(x-y)
else: # 무조건 일직선으로 가는 게 이득인 경우
  time = w*(x+y)

print(time)
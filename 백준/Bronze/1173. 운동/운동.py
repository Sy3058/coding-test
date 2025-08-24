N, m, M, T, R = map(int, input().split())
et = 0 # 운동한 시간 (== N이 되어야함)
time = 0
cur_m = m

if m + T > M: # 운동을 할 수 없는 경우
  print(-1)
  exit()

while et < N:
  if cur_m + T <= M: # 운동을 한 후에 맥박이 M보다 작거나 같다면 운동 가능
    time += 1 # 시간 추가
    et += 1 # 운동했으니 운동 시간 추가
    cur_m += T # 맥박 변경
  
  else: # 운동을 할 수 없다면
    if cur_m - R >= m: # 휴식한 후에 맥박이 m보다 크거나 같다면 휴식 가능
      cur_m -= R
    else:
      cur_m = m
    time += 1

print(time)
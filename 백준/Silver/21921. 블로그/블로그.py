N, X = map(int, input().split()) # 지난 일수, 기간
vs = list(map(int, input().split())) # 방문자 수

window = sum(vs[0:X]) # X일 동안의 합
ans = window # 방문자 수
cnt = 1 # 기간의 수

if max(vs) == 0:
  print('SAD')
else:
  for i in range (X, N):
    window += vs[i] - vs[i-X]
    if window > ans:
      ans = window
      cnt = 1
    elif window == ans:
      cnt += 1
  
  print(ans)
  print(cnt)
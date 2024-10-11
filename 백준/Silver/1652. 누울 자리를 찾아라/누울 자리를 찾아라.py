n = int(input())
arr = []
wcnt = 0 # 가로로 누울 수 있는 경우
lcnt = 0 # 세로로 누울 수 있는 경우

# 배열 입력
for _ in range (n):
  seat = input()
  arr.append(seat)

# 가로
for i in range (n):
  cnt1 = 0 # 가로를 위한 카운트
  for j in range (n):
    if arr[i][j] == '.':
      cnt1 += 1
    else:
      if cnt1 >= 2:
        wcnt += 1
      cnt1 = 0
  if cnt1 >= 2: # 마지막까지 '.'이 이어진 경우
    wcnt += 1

# 세로
for i in range (n):
  cnt2 = 0 # 세로를 위한 카운트
  for j in range (n):
    if arr[j][i] == '.':
      cnt2 += 1
    else:
      if cnt2 >= 2:
        lcnt += 1
      cnt2 = 0
  if cnt2 >= 2: # 마지막까지 '.'이 이어진 경우
    lcnt += 1

print(wcnt, lcnt)
from collections import deque

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (n)]
rotated_arr = [row[:] for row in arr] # 원본 복사

# 실질적 회전 횟수 = 회전 % (회전시켜야하는 배열 길이)
for idx in range (min(n, m) // 2):
  arr_length = ((m-idx*2) + (n-idx*2)) * 2 - 4
  rotation = r % arr_length
  cur_arr = deque([])

  # 윗줄: 오른쪽 끝(코너) 직전까지
  for j in range(idx, m - idx - 1):
      cur_arr.append(arr[idx][j])
  # 오른쪽: 맨 아래(코너) 직전까지
  for i in range(idx, n - idx - 1):
      cur_arr.append(arr[i][m - idx - 1])
  # 아래: 왼쪽 끝(코너) 직전까지 - 역방향
  for j in range(m - idx - 1, idx, -1):
      cur_arr.append(arr[n - idx - 1][j])
  # 왼쪽: 맨 위(코너) 직전까지 - 역방향
  for i in range(n - idx - 1, idx, -1):
      cur_arr.append(arr[i][idx])

  # 반시계 방향으로 현재 배열을 회전
  cur_arr.rotate(-rotation)

  k = 0
  # 윗줄
  for j in range(idx, m - idx - 1):
      rotated_arr[idx][j] = cur_arr[k]
      k += 1
  # 오른쪽
  for i in range(idx, n - idx - 1):
      rotated_arr[i][m - idx - 1] = cur_arr[k]
      k += 1
  # 아래
  for j in range(m - idx - 1, idx, -1):
      rotated_arr[n - idx - 1][j] = cur_arr[k]
      k += 1
  # 왼쪽
  for i in range(n - idx - 1, idx, -1):
      rotated_arr[i][idx] = cur_arr[k]
      k += 1
  
for i in range (n):
  print(*rotated_arr[i])
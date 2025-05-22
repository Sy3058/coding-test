for _ in range (10):
  tc = int(input())
  arr = list(list(map(int, input().split())) for _ in range (100))

  ms = 0 # max sum
  # 가로
  for i in range (100):
    ms = max(ms, sum(arr[i]))
  
  # 세로
  for i in range (100):
    hap = 0
    for j in range (100):
      hap += arr[j][i]
    ms = max(ms, hap)

  # 대각선
  rdhap = 0 # 오른쪽 하향 대각선
  for i in range (100):
    rdhap += arr[i][i]
  ms = max(ms, rdhap)

  # 오른쪽 상향 대각선
  ruhap = 0
  for i in range (100):
    ruhap += arr[i][99-i]
  ms = max(ms, ruhap)

  print("#%d %d"%(tc, ms))
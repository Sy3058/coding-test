a, b = input().split()
cnt = 0
if len(a) == len(b): # 연산을 할 수 없으므로 바로 비교
  for i in range (len(a)):
    if a[i] != b[i]:
      cnt += 1
  print(cnt)

else:
  min_diff = float('inf')
  for i in range (len(b) - len(a) + 1):
    cnt = 0
    for j in range (len(a)):
      if a[j] != b[i+j]:
        cnt += 1
    min_diff = min(min_diff, cnt)
  print(min_diff)
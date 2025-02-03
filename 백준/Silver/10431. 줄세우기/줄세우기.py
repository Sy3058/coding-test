import sys
input = sys.stdin.readline

p = int(input())
for _ in range (p):
  li = list(map(int, input().split()))
  t = li[0]
  h = li[1:]
  cnt = 0
  for i in range (19):
    for j in range (i+1, 20):
      if h[i] > h[j]: # 앞에 선 사람이 더 크면 자리 바꿈
        h[i], h[j] = h[j], h[i]
        cnt += 1

  print(t, cnt)
  

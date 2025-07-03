T = int(input())

for tc in range (1, T+1):
  N, M = map(int, input().split())
  Ai = list(map(int, input().split()))
  Bj = list(map(int, input().split()))
  ans = 0

  if N == M:
    hap = 0
    for i in range (N):
      hap += Ai[i] * Bj[i]
    ans = hap

  elif N > M:
    for i in range (N-M+1):
      hap = 0
      for j in range (i, i+M):
        hap += Ai[j] * Bj[j-i]
      ans = max(hap, ans)
  
  else:
    for i in range (M-N+1):
      hap = 0
      for j in range (i, i+N):
        hap += Ai[j-i] * Bj[j]
      ans = max(hap, ans)
  
  print(f'#{tc} {ans}')
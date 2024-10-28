N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0

for i in range (N-2):
  for j in range (i+1, N-1):
    for k in range (j+1, N):
      hap = cards[i] + cards[j] + cards[k]
      if hap == M:
        ans = M
        break
      elif hap > ans and hap < M:
        ans = hap
  
print(ans)
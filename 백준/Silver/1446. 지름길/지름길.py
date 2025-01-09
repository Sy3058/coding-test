import sys
input = sys.stdin.readline

n, d = map(int, input().split())
sc = []
dp = [i for i in range (d+1)]

for _ in range (n):
  s, e, l = map(int, input().split())
  if e > d: # 돌아올 수 없으므로 초과하면 안됨
    continue
  
  elif e - s <= l: # 지름길이 더 오래 걸리면 굳이 사용할 필요 없음
    continue

  else:
    sc.append((s, e, l))
    
sc.sort(key = lambda x:x[1], reverse = True)
sc.sort(key = lambda x:(x[0], x[2]))

for i in range (len(sc)):
  for j in range (d+1):
    if sc[i][0] == j:
      end = sc[i][1]
      dp[end] = min(dp[j] + sc[i][2], dp[end-1]+1, dp[end])
    else:
      dp[j] = min(dp[j], dp[j-1] + 1)

print(dp[-1])
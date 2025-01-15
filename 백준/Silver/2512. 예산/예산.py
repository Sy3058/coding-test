import sys
input = sys.stdin.readline

n = int(input()) # 지방의 수
budget = list(map(int, input().split())) # 예산
tb = int(input()) # 총예산
budget.sort()

def solution():
  if sum(budget) <= tb:
    return budget[-1]
  
  l = min(tb//n, budget[0])
  r = budget[-1]
  ans = l

  while l < r-1:
    hap = 0
    m = (l+r)//2
    for i in range (n):
      if budget[i] <= m:
        hap += budget[i]
      else:
        hap += m * (n-i)
        break
    
    if hap == tb:
      return m
    
    if hap > tb:
      r = m
    else:
      l = m
      ans = max(m, ans)

  return ans

ans = solution()
print(ans)

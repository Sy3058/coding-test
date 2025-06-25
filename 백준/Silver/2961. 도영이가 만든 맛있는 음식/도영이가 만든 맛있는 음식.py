import sys
input = sys.stdin.readline

def cook(idx, s, b, use):
  global ans

  if idx == n:
    if use == 0:
      return
    
    res = abs(s - b)
    ans = min(ans, res)
    return
  
  # idx번째 재료 사용
  cook(idx + 1, s * ing[idx][0], b + ing[idx][1], use + 1)

  # idx번째 재료 미사용
  cook(idx + 1, s, b, use)

n = int(input())
ing = [list(map(int, input().split())) for _ in range (n)]

ans = float('inf')

cook(0, 1, 0, 0)
print(ans)
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def sol(idx, hap):
  global cnt

  if idx >= n:
    return
  
  hap += arr[idx]

  if hap == s:
    cnt += 1
  
  # 현재 idx를 선택한 경우
  sol(idx+1, hap)

  # 현재 idx를 선택하지 않은 경우
  sol(idx+1, hap - arr[idx])

sol(0, 0)
print(cnt)
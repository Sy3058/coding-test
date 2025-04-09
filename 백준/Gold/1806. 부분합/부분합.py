import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
hap = arr[l]
ml = float('inf') # 최소 길이

while r < n:
  if hap < s:
    if r == n-1:
      break
    r += 1
    hap += arr[r]
  
  else:
    ml = min(ml, r-l+1) # 길이 갱신
    if r == l: # 원소 하나가 s 이상일 때
      break # 무조건 하나일 때가 가장 짧으므로 더 진행할 필요가 없음

    else:
      hap -= arr[l]
      l += 1

if ml == float('inf'):
  print(0)
else:
  print (ml)
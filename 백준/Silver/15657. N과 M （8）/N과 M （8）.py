import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()

def sol(ans):
  if len(ans) == m:
    print(' '.join(map(str, ans)))
    return
  
  for i in range (len(arr)):
    if len(ans) == 0:
      ans.append(arr[i])
      sol(ans)
      ans.pop()

    elif len(ans) != 0 and ans[-1] <= arr[i]:
      ans.append(arr[i])
      sol(ans)
      ans.pop()

ans = []
sol(ans)
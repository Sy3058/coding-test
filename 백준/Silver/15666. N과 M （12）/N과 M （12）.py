import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()
al = set()

def sol(ans):
  if len(ans) == m:
    answer = ' '.join(map(str, ans))
    if answer not in al:
      print(answer)
    return
  
  for i in range (len(arr)):
    if len(ans) == 0:
      ans.append(arr[i])
      sol(ans)
      ans.pop()
    
    else:
      if ans[-1] <= arr[i]:
        ans.append(arr[i])
        sol(ans)
        ans.pop()

sol([])
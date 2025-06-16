import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(set((map(int, input().split()))))
arr.sort()
ans = []

def sol(ans):
  if len(ans) == m:
    print(' '.join(map(str, ans)))
    return
  
  for i in range (len(arr)):
    ans.append(arr[i])
    sol(ans)
    ans.pop()

sol(ans)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(set(map(int, input().split())))
arr.sort()
al = set() # answer list

def sol(ans):
  if len(ans) == m:
    answer = ' '.join(map(str, ans))
    if answer not in al:
      print(answer)
      al.add(answer)
    return
  
  for i in range (len(arr)):
    ans.append(arr[i])
    sol(ans)
    ans.pop()
  
sol([])
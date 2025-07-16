a, b = map(int, input().split())
cnt = 0
flag = False

def dfs(num, cnt):
  if num == b:
    flag = True
    print(cnt + 1)
    exit()
  
  if num > b:
    cnt -= 1
    return
  
  dfs(num * 2, cnt + 1)
  dfs(10 * num + 1, cnt + 1)

dfs(a, 0)
if not flag:
  print(-1)
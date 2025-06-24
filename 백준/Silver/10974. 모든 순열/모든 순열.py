n = int(input())
al = []
visited = [False] * (n+1)

def sol(ans):
  if len(ans) == n:
    answer = ' '.join(map(str, ans))
    if answer not in al:
      print(answer)
      al.append(answer)
    return
  
  for i in range (1, n+1):
    if not visited[i]:
      ans.append(i)
      visited[i] = True
      sol(ans)
      ans.pop()
      visited[i] = False

sol([])
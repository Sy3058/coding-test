def dfs(depth):
  global ans

  if depth == cnt: # 제시된 횟수만큼 교환을 완료하면 종료
    ans = max(ans, int(''.join(arr)))
    return
  
  for i in range (len(arr)):
    for j in range (i + 1, len(arr)):
      arr[i], arr[j] = arr[j], arr[i] # 자리 바꿈
      tmp = int(''.join(arr))

      if (depth, tmp) not in visited: # 이미 확인한 수라면 통과
        visited.append((depth, tmp))
        dfs(depth + 1)
      
      arr[i], arr[j] = arr[j], arr[i] # 확인 끝나면 다시 돌려놓기

T = int(input())
for tc in range (1, T + 1):
  num, cnt = map(int, input().split())
  arr = list(str(num))
  visited = []
  ans = 0
  dfs(0)

  print("#%d %d"%(tc, ans))
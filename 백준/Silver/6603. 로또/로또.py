test = list(map(int, input().split()))

def dfs():
  if len(arr) == 6: # 6개를 뽑아냄
    print(' '.join(map(str, arr)))
    return
  
  for i in range (k):
    if visited[i]:
      continue

    if not arr:
      visited[i] = True
      arr.append(num_list[i])
      dfs()
      arr.pop()
      visited[i] = False
    else:
      if num_list[i] > arr[-1]:
        visited[i] = True
        arr.append(num_list[i])
        dfs()
        arr.pop()
        visited[i] = False

while test[0] != 0:
  k = test[0]
  num_list = test[1:]
  visited = [False] * k
  arr = []
  dfs()
  print('')

  test = list(map(int, input().split()))
import sys
input = sys.stdin.readline

n = int(input())
arr = {}
for i in range (1, n+1):
  arr[i] = int(input())
result = []

def dfs(s, c, visited, path):
  if visited[c]: # if c is already visited
    if c == s: # if it came back to starting point, than it's cycle
      return path # return path
    else:
      return [] # return empty array if it's not cycle
  
  visited[c] = True
  path.append(c) # append current to path
  return dfs(s, arr[c], visited, path)

for i in range (1, n+1):
  visited = [False] * (n+1)
  cycle = dfs(i, i, visited, [])
  result.extend(cycle)

result = list(set(result)) # remove duplicates
print(len(result))
for num in sorted(result):
  print(num)
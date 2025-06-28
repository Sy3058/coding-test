import sys
input = sys.stdin.readline

k = int(input())
signs = list(input().split())
maxans = 0
minans = float('inf')

def sol(ans, idx, visited):
  global maxans, minans
  if idx == k:
    answer = int(''.join(map(str, ans)))
    maxans = max(maxans, answer)
    minans = min(minans, answer)
    return
  
  for i in range (10):
    if not visited[i]:
      if signs[idx] == '<' and ans[-1] < i:
        ans.append(i)
        visited[i] = True
        sol(ans, idx + 1, visited)
        ans.pop()
        visited[i] = False
      
      elif signs[idx] == '>' and ans[-1] > i:
        ans.append(i)
        visited[i] = True
        sol(ans, idx + 1, visited)
        visited[i] = False
        ans.pop()

for i in range (10):
  visited = [False] * 10
  visited[i] = True
  sol([i], 0, visited)

if len(str(maxans)) == k:
  maxans = '0' + str(maxans)

if len(str(minans)) == k:
  minans = '0' + str(minans)
  
print(maxans)
print(minans)
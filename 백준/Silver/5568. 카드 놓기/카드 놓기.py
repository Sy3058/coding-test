import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
card = list(int(input()) for _ in range (n))
al = set() # answer list

def sol(ans, visited):
  if len(ans) == k:
    answer = ''.join(map(str, ans))
    al.add(answer)
  
  for i in range (n):
    if not visited[i]:
      ans.append(card[i])
      visited[i] = True
      sol(ans, visited)
      ans.pop()
      visited[i] = False

visited = [False] * n
sol([], visited)
print(len(al))
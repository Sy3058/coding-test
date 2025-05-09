import sys
input = sys.stdin.readline

vowel = {'a', 'e', 'i', 'o', 'u'}
l, c = map(int, input().split())
alpha = list(input().split())
alpha.sort()
visited = [False] * c # 알파벳 순서대로 방문 확인
pw = [] # 암호

def dfs(depth, idx, pw):
  if depth == l:
    ans = set(pw)
    if vowel&ans and len(ans - vowel) >= 2: # 최소 한 개의 모음과 최소 두 개의 자음 조건
      print(''.join(pw))

    return

  for i in range (idx, c): # 백트래킹
    if not visited[i]:
      visited[i] = True # i번째 알파벳 방문처리
      pw.append(alpha[i]) # i번째 알파벳 추가
      dfs(depth + 1, i + 1, pw) # 깊이 증가
      visited[i] = False # 확인 끝났으므로 미방문처리
      pw.pop() # 사용한 암호 제거

dfs(0, 0, pw)
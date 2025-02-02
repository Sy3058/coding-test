import sys
input = sys.stdin.readline

m = int(input())
S = set()
for _ in range (m):
  com = list(input().split())

  if com[0] == 'add':
    S.add(int(com[1]))
  
  elif com[0] == 'remove':
    S.discard(int(com[1]))
  
  elif com[0] == 'check':
    print(1) if int(com[1]) in S else print(0)
  
  elif com[0] == 'toggle':
    S.remove(int(com[1])) if int(com[1]) in S else S.add(int(com[1]))
  
  elif com[0] == 'all':
    S = set([i+1 for i in range (20)])
  
  else:
    S = set()

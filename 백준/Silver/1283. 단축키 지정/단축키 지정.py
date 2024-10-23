import sys

N = int(sys.stdin.readline()) # number of options
sc = [] # short cuts

for _ in range (N):
  words = list(sys.stdin.readline().split())
  flag1 = False # 1, 2번 조건 확인용 flag

  for i in range (len(words)):
    if words[i][0].upper() not in sc: # 1, 2번 조건
      sc.append(words[i][0].upper())
      flag1 = True
      words[i] = '[' + words[i][0] + ']' + words[i][1:]
      print(' '.join(words))
      break

  if not flag1: # 위에서 추가되지 않았다면
    for i in range(len(words)):
      flag2 = False # 3번 조건 확인용
      for j in range(len(words[i])):
        if words[i][j].upper() not in sc:
          sc.append(words[i][j].upper())
          flag1 = True
          flag2 = True
          words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j+1:]
          print(' '.join(words))
          break
      if flag2: # 조건3을 만족했다면 더 돌지 않아도 됨
        break
  
  if not flag1: # 모든 조건을 만족하지 않음
    print(' '.join(words))
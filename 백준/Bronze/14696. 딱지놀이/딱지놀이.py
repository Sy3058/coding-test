# 별의 개수 > 동그라미 개수 > 네모 개수 > 세모 개수 (모두 같으면 무승부)
import sys
input = sys.stdin.readline

n = int(input())
for _ in range (n):
  alist = list(map(int, input().split()))[1:]
  blist = list(map(int, input().split()))[1:]

  adict = {i:0 for i in range (1, 5)}
  bdict = {i:0 for i in range (1, 5)}

  for num in alist:
    adict[num] += 1
  
  for num in blist:
    bdict[num] += 1

  # 별 개수 비교
  if adict[4] > bdict[4]:
    print('A')
    continue
  
  elif adict[4] < bdict[4]:
    print('B')
    continue

  if adict[3] > bdict[3]:
    print('A')
    continue

  elif adict[3] < bdict[3]:
    print('B')
    continue

  if adict[2] > bdict[2]:
    print('A')
    continue

  elif adict[2] < bdict[2]:
    print('B')
    continue

  if adict[1] > bdict[1]:
    print('A')
    continue

  elif adict[1] < bdict[1]:
    print('B')
    continue

  print('D')
import sys
input = sys.stdin.readline

scores = [int(input()) for _ in range (10)]
hap = 0

if scores[0] > 200:
  print(0)
elif scores[0] >= 100:
  print(scores[0])
else:
  for i in range (10):
    hap += scores[i]
    if hap >= 100:
      break

  if hap - 100 > 100 - (hap - scores[i]):
    print(hap - scores[i])
  else:
    print(hap)
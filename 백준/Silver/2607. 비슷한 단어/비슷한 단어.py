import sys
from collections import Counter

n = int(sys.stdin.readline())

words = []
cnt = 0 # 비슷한 단어의 개수수
for _ in range (n):
  w = list(sys.stdin.readline().strip())
  words.append((Counter(w), len(w)))

for i in range (1, n):
  if words[0][1] >= words[i][1]:
    tmp = words[0][0] - words[i][0]
    hap = sum(tmp.values())
  else:
    tmp = words[i][0] - words[0][0]
    hap = sum(tmp.values())
  
  if hap <= 1:
    cnt += 1

print(cnt)
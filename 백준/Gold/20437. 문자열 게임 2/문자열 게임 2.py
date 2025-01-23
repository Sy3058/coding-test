import sys
from collections import Counter
input = sys.stdin.readline

t = int(input())

for _ in range (t):
  w = list(input().strip())
  k = int(input())

  wc = Counter(w)
  kw = {key: cnt for key, cnt in wc.items() if cnt >= k} # 기준 개수 이상인 알파벳만 확인

  if kw:
    tc = set(kw.keys()) # target char
    result = {c: [] for c in tc}

    for idx, char in enumerate(w):
      if char in tc:
        result[char].append(idx)

    ms = 10000 # 가장 짧은 문자열
    mb = 0 # 가장 긴 문자열

    for c in tc:
      ti = result[c] # target index
      for i in range (len(ti) - k + 1):
        nsw = ti[k+i -1] - ti[i] + 1 # next sliding window (문자열의 길이이므로 1을 더해줘야함)
        ms = min(ms, nsw)
        mb = max(mb, nsw)

    print(ms, mb)
  
  else:
    print(-1)

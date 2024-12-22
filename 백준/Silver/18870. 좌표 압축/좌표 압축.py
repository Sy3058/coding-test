import sys

n = int(sys.stdin.readline())
xs = list(map(int, sys.stdin.readline().split()))

sxs = sorted(list(set(xs)))
dxs = dict(zip(sxs, list(range(len(xs))))) # 정렬된 리스트에서 인덱스 == Xi > Xj를 만족하는 Xj의 개수

for i in xs:
  print(dxs[i], end = ' ')
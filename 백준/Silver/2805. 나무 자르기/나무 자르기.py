import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

def p_cut(trees, h, m):
  # 절단기 높이가 h일 때 나무 길이가 m 이상인지 확인
  hap = 0
  for t in trees:
    if t > h:
      hap += t - h
  return hap >= m

low, high = 0, max(trees)
result = 0

while low <= high:
  mid = (low + high) // 2
  if p_cut(trees, mid, m):
    result = mid # 조건을 만족하는 경우 현재 높이 저장
    low = mid + 1 # 가장 높은 높이를 찾아야하므로 다시 탐색
  else:
    high = mid - 1

print(result)
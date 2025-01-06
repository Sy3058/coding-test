import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

def bi_search(A):
  sub = []
  for x in A:
    pos = bisect_left(sub, x) # x가 들어갈 위치
    if pos == len(sub):
      sub.append(x) # 새로운 숫자를 추가
    else:
      sub[pos] = x # 기존 숫자를 갱신
  
  return len(sub)

print(bi_search(A))
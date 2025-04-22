import sys
input = sys.stdin.readline

n = int(input())
chain = list(map(int, input().split()))
chain.sort()

def solution(n, chain):
  uc = 0 # used chain

  for c in chain:
    if c == n - 1: # 체인 하나를 해체하면 모든 체인을 연결할 수 있음
      return uc + c
    
    elif c > n - 1:
      return uc + n - 1

    else:
      n -= (c + 1) # 길이가 c인 체인을 해체하면 c + 1개만큼 연결 가능
      uc += c

print(solution(n, chain))
import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

def count_fruit(n, s):
  cnt = 0
  l = 0
  fc = {} # 과일의 개수

  for r in range (n):
    fc[s[r]] = fc.get(s[r], 0) + 1 # 오른쪽 포인터를 이동시키며 과일 추가

    while len(fc) > 2: # 존재하는 과일의 종류가 2개 이상이 되면
      fc[s[l]] -= 1 # 왼쪽 포인터에 해당하는 과일의 개수를 줄임
      if fc[s[l]] == 0: # 한가지 과일의 개수가 0개가 되면 그 과일은 딕셔너리에서 삭제
        del fc[s[l]]
      l += 1 # 왼쪽 포인터를 하나씩 오른쪽으로 이동
    
    cnt = max(cnt, r - l + 1)
  
  return cnt

if len(set(s)) <= 2:
  print(n)
else:
  print(count_fruit(n, s))
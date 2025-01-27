import sys
input = sys.stdin.readline

n, l = map(int, input().split())

def solution(n, l):
  ans = []
  if l == 2:
    if n%2 == 1:
      ans = [n//2, n//2 + 1]
      return ans
    else:
      l += 1

  while l < 101:
    if l%2 == 0: # 짝수
      x = n/l - l/2 + 1/2
      if x - int(x) == 0 and x >= 0:
        for i in range (int(x), int(x)+l):
          ans.append(i)
        return ans
    else: # 홀수
      if n%l == 0:
        if n//l - l//2 >= 0:
          for i in range (n//l - l//2, n//l + l//2 + 1):
            ans.append(i)
          return ans
    l += 1
  
  return [-1]

ans = solution(n, l)
print(' '.join(map(str, ans)))
import sys
input = sys.stdin.readline

na, nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

ans = list(a-b)
ans.sort()
print(len(ans))
if ans:
  print(*ans)
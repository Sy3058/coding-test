import sys
input = sys.stdin.readline

n, j, h = map(int, input().split())
a = min(j, h)
b = max(j, h)
cnt = 1
while True:
  if a%2 == 1 and b == a+1: # 작은 쪽이 홀수고 큰 쪽이 그 다음 오는 수여야 함
    break
  if a%2 == 1:
    a = a//2 + 1
  else:
    a //= 2
  if b%2 == 1:
    b = b//2 + 1
  else:
    b //= 2
  cnt += 1

print(cnt)
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0 # 낙찰받은 지면의 개수
diff = []
for i in range (n):
  a, b = map(int, input().split()) # 입찰가, 최고가
  if a >= b: # 입찰가가 최고가보다 큰 경우
    cnt += 1
  else:
    # diff만큼 올려야 지면을 낙찰받을 수 있음
    diff.append(b - a)

diff.sort()
if cnt >= k:
  print(0)
else:
  print(diff[k - cnt -1])
import sys
input = sys.stdin.readline

l = int(input()) # 롤 케이크의 길이
n = int(input()) # 방청객의 수
cake = [0] * (l+1)
exp = (0, 0) # 기대한 개수, 방청객 번호
real = (0, 0) # 실제 받은 개수, 방청객 번호
for num in range (1, n+1):
  p, k = map(int, input().split())
  want = k - p + 1
  cnt = 0
  if want > exp[0]:
    exp = (want, num)

  for i in range (p, k+1):
    if cake[i] == 0:
      cake[i] = num
      cnt += 1
  
  if cnt > real[0]:
    real = (cnt, num)
  
print(exp[1])
print(real[1])
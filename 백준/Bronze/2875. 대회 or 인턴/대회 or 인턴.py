n, m, k = map(int, input().split())

cnt = 0

# 팀을 만드는 게 가능한 동안 n과 m의 수를 줄이면서 팀의 수 늘리기
while n >= 2 and m >= 1 and n + m >= k + 3:
  n -= 2
  m -= 1
  cnt += 1
print(cnt)
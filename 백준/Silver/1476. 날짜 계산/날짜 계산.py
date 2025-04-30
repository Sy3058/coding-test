import sys
input = sys.stdin.readline

E, S, M = map(int, input().split()) # 16, 28, 19
year = S
while year < 10000:
  e = year % 15
  s = year % 28
  m = year % 19
  if e == 0: e = 15
  if s == 0: s = 28
  if m == 0: m = 19
  if e == E and s == S and m == M:
    break

  year += 28 # 가장 큰 값을 기준으로 값 증가시키기

print(year)
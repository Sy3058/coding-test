import sys

n = int(sys.stdin.readline())
s = (n//3)%2 # 몫이 짝인지 홀인지 확인
r = n%3 # 나머지 확인

if s == 0:
  if r%2 == 0:
    print('CY')
  else:
    print('SK')
else:
  if r%2 == 0:
    print('SK')
  else:
    print('CY')
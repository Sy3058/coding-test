import sys
input = sys.stdin.readline

n = int(input())
f = int(input())

rest = n%f
if (n%100)%f >= rest:
  last = (n%100)%f - rest
else:
  last = (n%100)%f + f - rest
print('%02d'%last) # 00형태로 출력
import sys

num_li = list(map(int, sys.stdin.readline().split()))
num_li.sort()

a = num_li[0]
b = num_li[1]
c = num_li[2]

if a + b > c: # 삼각형을 만들 수 있는 경우
  print(a+b+c)

else: # 삼각형을 만들 수 없는 경우 c의 최댓값 == a+b-1
  print(2*(a+b) - 1)
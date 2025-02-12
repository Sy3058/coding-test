import sys
input = sys.stdin.readline

n = list(map(int, list(input().strip())))
n.sort(reverse = True)

if sum(n)%3 != 0: # 3의 배수이려면 각 자릿수의 합이 3이어야함
  print(-1)
elif n[-1] != 0: # 10의 배수이려면 마지막 자리가 0이어야함
  print(-1)
else:
  print(*n, sep='')
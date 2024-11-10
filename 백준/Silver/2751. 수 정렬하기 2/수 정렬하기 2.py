import sys

N = int(sys.stdin.readline())
num_list = []

for _ in range (N):
  num = int(sys.stdin.readline())
  num_list.append(num)

num_list.sort()
print('\n'.join(map(str, num_list)))
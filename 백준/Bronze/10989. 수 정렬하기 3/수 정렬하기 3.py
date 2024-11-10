import sys

N = int(sys.stdin.readline())
num_list = [i for i in range (1, 10001)]
num_dict = {key:0 for key in num_list}

for _ in range (N):
  num = int(sys.stdin.readline())
  num_dict[num] += 1

for i in range (1, 10001):
  for j in range (num_dict[i]):
    print(i)
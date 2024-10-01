n = int(input())
num_list = list(map(int, input().split()))

if n == 1:
  print(num_list[0]**2)
else:
  print(max(num_list) * min(num_list))
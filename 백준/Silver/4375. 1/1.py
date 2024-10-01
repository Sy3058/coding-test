# 4375

import sys

num_list = []

try:
  while True:
    num = int(input())
    ans = 1
    while ans % num != 0:
      ans = ans*10 + 1
    
    print(len(str(ans)))
except EOFError:
  pass
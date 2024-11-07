import sys
from collections import deque

S = list(sys.stdin.readline().strip())

zero = S.count('0') // 2
one = S.count('1') // 2

for i in range (one): # 앞에있는 1부터 삭제해야함
  S.remove('1')

S.reverse()

for j in range (zero): # 뒤에있는 0부터 삭제해야함
  S.remove('0')

S.reverse()

print(''.join(S))
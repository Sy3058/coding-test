import sys
from itertools import combinations
input = sys.stdin.readline

'''
기본 개념
ord(문자) => 문자에 해당하는 유니코드 정수 반환
chr(정수) => 정수에 해당하는 유니코드 문자 반환
a << b => 변수의 값을 지정된 값의 비트만큼 왼쪽으로 이동
a | b => OR 연산 (비트가 둘 중 하나라도 참이면 만족)
~a => NOT 연산 (0 -> 1, 1 -> 0)
'''

n, k = map(int, input().split())

# 필수 글자
basic = {'a', 'n', 't', 'i', 'c'}

words = []
for _ in range (n):
  s = input().strip()
  bit = 0
  for ch in set(s):
    bit |= (1 << (ord(ch) - ord('a')))
  words.append(bit) # bit가 word에 해당하는 알파벳의 정보를 담고 있음

# 적어도 antic은 읽어야만 글자를 읽을 수 있음
if k < 5:
  print(0)
  exit()

# 모든 알파벳을 배운 것이므로 모두 읽을 수 있음
if k == 26:
  print(n)
  exit()

bb = 0 # basic bit
for ch in basic:
  bb |= (1 << (ord(ch) - ord('a')))

# 후보 알파벳
alpha = [i for i in range (26) if chr(i + ord('a')) not in basic] # ord(ch) - ord('a')에 해당하는 값이 i
mw = 0 # 읽을 수 있는 최대 글자 수

# 후보군 중 k-5개의 알파벳의 조합
for comb in combinations(alpha, k-5):
  lb = bb # learn bit
  for c in comb:
    lb |= (1 << c)
  
  cnt = 0
  for word in words:
    if word & ~lb == 0: # 배운적 없는 알파벳과 word의 합집합이 0이면 모든 알파벳을 배운 것
      cnt += 1
  mw = max(mw, cnt)

print(mw)
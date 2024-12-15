import sys

n = int(sys.stdin.readline())

i = 1
num = 666

while i <= n:
  if '666' in str(num):
    i += 1
  num += 1

print(num - 1)
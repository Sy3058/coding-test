import sys

n = list(sys.stdin.readline().strip())
n.sort(reverse=True)
print(''.join(n))
import sys
n1 = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
n2 = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
arr = [0] * n2

set_A = set(A)

for i in range (n2):
    if M[i] in set_A:
        print(1)
    else:
        print(0)
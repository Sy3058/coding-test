import sys
from collections import Counter

n = int(sys.stdin.readline())
nc = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mc = list(map(int, sys.stdin.readline().split()))

card_count = Counter(nc)

answer = [str(card_count[num]) for num in mc]

print(' '.join(answer))
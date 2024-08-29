import sys
from collections import Counter

def check(string):
  for i in T:
    if i in string and string[i] != 0:
      string[i] -= 1
    else:
      return False
  return True

T = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
books = []
for i in range (N):
  price, title = sys.stdin.readline().split()
  books.append([int(price), Counter(title)])

result = float('inf')

for i in range (1 << N):
  price = 0
  alpha = Counter()
  for j in range (N):
    if (i & 1 << j):
      price += books[j][0]
      alpha += books[j][1]
  
  if check(alpha):
    result = min(result, price)

print(result if result != float('inf') else -1)
import sys

def gcd(a, b): # 두 수의 최대 공약수
  while b > 0:
    a, b = b, a % b
  return a

n = int(sys.stdin.readline()) # 심어져 있는 가로수의 수
tree = [int(sys.stdin.readline()) for _ in range (n)]

dis = tree[-1] - tree[0] # 나무들 사이의 거리
diff = set()

for i in range (1, n):
  d = tree[i] - tree[i-1]
  diff.add(d)

ld = list(diff)
mingcd = ld[0]

for j in range (1, len(ld)):
  mingcd = gcd(mingcd, ld[j])

ans = (dis//mingcd + 1) - n # 최소 간격으로 심을 때 필요한 나무의 수 - 현재 심어져 있는 나무의 수
print(ans)
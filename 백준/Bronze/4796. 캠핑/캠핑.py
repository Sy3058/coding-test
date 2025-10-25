import sys
input = sys.stdin.readline

c = 1
while True:
  l, p, v = map(int, input().split())
  if not l and not p and not v:
    break
  if v % p >= l:
    print(f"Case {c}: {v//p * l + l}")
  else:
    print(f"Case {c}: {v//p * l + v%p}")
  c += 1
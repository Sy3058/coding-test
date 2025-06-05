import sys
input = sys.stdin.readline

n = int(input())
flag = False # 만났는지 확인
pl = set()

for _ in range (n):
  a, b = input().split()
  if a == "ChongChong" or b == "ChongChong":
    flag = True
    pl.add(a)
    pl.add(b)

  if flag and (a in pl or b in pl):
    pl.add(a)
    pl.add(b)

print(len(pl))
n = int(input())

for _ in range (n):
  s1, s2 = input().split()
  s1, s2 = list(s1), list(s2)
  c1, c2 = set(s1), set(s2)
  if len(s1) == len(c1) and len(s2) == len(c2): # 중복이 없는 경우
    if c1 == c2:
      print("Possible")
    else:
      print("Impossible")
  else:
    s1.sort()
    s2.sort()
    if s1 == s2:
      print("Possible")
    else:
      print("Impossible")
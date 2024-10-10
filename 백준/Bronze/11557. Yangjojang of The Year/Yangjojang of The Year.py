t = int(input()) # test case
for _ in range (t):
  n = int(input()) # number of school
  stack = []
  for _ in range (n):
    s, a = input().split() # school & alcohol
    a = int(a)
    if stack:
      if a > stack[1]:
        stack = [s, a]
    else: # stack이 없는 상태
      stack = [s, a]
  print(stack[0])
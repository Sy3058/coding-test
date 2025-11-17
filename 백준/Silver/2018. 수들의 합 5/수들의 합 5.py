n = int(input())
e = 0
hap = 0
cnt = 0

for s in range (0, n):
  while hap < n and e < n:
    hap += e + 1
    e += 1
  
  if hap == n:
    cnt += 1
  
  hap -= s + 1
print(cnt)
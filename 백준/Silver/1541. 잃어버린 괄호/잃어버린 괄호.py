import sys
input = sys.stdin.readline

formula = input().strip()
mf = formula.split('-')

for i in range (len(mf)):
  pf = mf[i].split('+')
  hap = 0
  for j in range (len(pf)):
    hap += int(pf[j])
  
  mf[i] = hap

ans = mf[0]
for i in range (1, len(mf)):
  ans -= mf[i]

print(ans)
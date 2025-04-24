import sys
input = sys.stdin.readline

digit = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]
for _ in range (3):
  digit.append(int(input()))

hap = 0
for i in range (13):
  if i%2 == 0:
    hap += digit[i] * 1
  
  else:
    hap += digit[i] * 3

print('The 1-3-sum is %d' %hap)
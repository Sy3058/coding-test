import sys
input = sys.stdin.readline

isbn = list(input().strip())
cm = 1 # 곱해야하는 값
m = {0:1, 1:3} # 짝수번째는 1을 곱하고 홀수번째는 3을 곱함
hap = 0
for i in range (12):
    if isbn[i] == '*':
        cm = m[i%2]
        continue
    hap += int(isbn[i]) * m[i%2]
    hap %= 10

if int(isbn[-1]) == 0:
    target = 0
else:
    target = 10 - int(isbn[-1])

for i in range (10):
    if (hap + i * cm) % 10 == target:
        print(i)
        break
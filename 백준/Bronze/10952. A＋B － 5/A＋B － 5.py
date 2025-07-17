import sys

li = sys.stdin.readlines()
for i in range (len(li)):
    a, b = map(int, li[i].split())
    if a + b == 0:
        break
    print(a+b)
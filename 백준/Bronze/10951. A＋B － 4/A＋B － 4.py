import sys

li = sys.stdin.readlines()
for i in range (len(li)):
    a, b = map(int, li[i].split())
    print(a+b)
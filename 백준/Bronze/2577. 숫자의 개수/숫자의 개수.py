import sys
input = sys.stdin.readline
nd = {i:0 for i in range (0, 10)}

a = int(input())
b = int(input())
c = int(input())
for x in str(a * b * c):
    nd[int(x)] += 1

for key, value in nd.items():
    print(value)
import sys
input = sys.stdin.readline

l = int(input())
s = input().strip()
h = 0

for i in range (l):
    h += (int(ord(s[i])) - 96) * (31 ** (i))
    h %= 1234567891

print(h)
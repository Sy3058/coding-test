import sys
input = sys.stdin.readline

for _ in range (int(input())):
    r, s = input().split()
    for i in range (len(s)):
        print(s[i]*int(r), end = '')
    print()

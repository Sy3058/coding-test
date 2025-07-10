import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
p = [i for i in range (8)]

for i in range (n):
    if arr[i].bit_count() != 2:
        continue

    s = []
    com = bin(arr[i])[2:].zfill(8)
    for j in range (8):
        if com[j] == '1':
            s.append(7-j)

    p[s[0]], p[s[1]] = p[s[1]], p[s[0]]

print(p[k])
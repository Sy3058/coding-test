import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
ad = [i for i in range (1, 9)]
dd = [i for i in range (8, 0, -1)]

if arr == ad:
    print('ascending')
elif arr == dd:
    print('descending')
else:
    print('mixed')

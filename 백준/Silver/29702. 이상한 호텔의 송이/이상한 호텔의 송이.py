import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range (t):
    n = int(input())
    binn = bin(n)[2:]
    floor = len(binn)
    path = ['1000000000000000001']
    room = 1

    for i in range (1, floor):
        if binn[i] == '1': # 오른쪽으로 내려감
            room = room * 2
        
        else: # 왼쪽으로 내려감
            room = room * 2 - 1

        path.append(str(i + 1) + str(room).zfill(18))
    
    for i in range (floor - 1, -1, -1):
        print(path[i])
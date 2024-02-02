import math

def rotate(arr, n):
    narr = [([0]*n) for i in range (n)]
    for i in range (len(arr)):
        for j in range (len(arr)):
            narr[len(arr)-1-j][i] = arr[i][j]
    return narr

def solution(n):
    x = 1
    arr = [[0 for i in range (n)] for i in range (n)]
    s = 0
    for k in range (math.ceil(n/2)):
        for i in range (4):
            for j in range (s, n-s):
                if arr[s][j] == 0:
                    arr[s][j] = x
                    x += 1
            arr = rotate(arr, n)
        s += 1
    return arr
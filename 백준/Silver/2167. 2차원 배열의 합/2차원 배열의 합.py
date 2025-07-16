import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (n)]
k = int(input())
sa = arr.copy()
for i in range (1, n):
    sa[i][0] += sa[i-1][0] 
for i in range (1, m):
    sa[0][i] += sa[0][i-1]

# 누적합
for i in range (1, n):
    for j in range (1, m):
        sa[i][j] = sa[i][j] + sa[i-1][j] + sa[i][j-1] - sa[i-1][j-1]

for _ in range (k):
    i, j, x, y = map(int, input().split())
    i -= 1; j -= 1; x -= 1; y -=1
    tmp = sa[x][y]

    if i > 0 and j > 0: # 가로 부분 세로 부분을 빼고 공통 부분을 더함
        tmp = tmp + sa[i-1][j-1] - sa[i-1][y] - sa[x][j-1]
    
    elif i > 0:
        tmp -= sa[i-1][y]
    
    elif j > 0:
        tmp -= sa[x][j-1]

    print(tmp)
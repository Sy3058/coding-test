import sys
input = sys.stdin.readline

k = int(input())
arr = [list(map(int, input().split())) for _ in range (6)]

w, w_idx = 0, 0
h, h_idx = 0, 0
for i in range (len(arr)):
    if arr[i][0] >= 3: # 방향이 남, 북이면 세로
        if h < arr[i][1]:
            h = arr[i][1] # 총 가로 길이
            h_idx = i # 총 가로 길이의 인덱스
    else:
        if w < arr[i][1]:
            w = arr[i][1] # 총 세로 길이
            w_idx = i # 총 세로 길이의 인덱스

# 가장 긴 가로&세로변 양 옆에 붙어있는 변들의 차이 = 뺄 사각형의 세로&가로

subw = abs(arr[(w_idx - 1) % 6][1] - arr[(w_idx + 1) % 6][1])
subh = abs(arr[(h_idx - 1) % 6][1] - arr[(h_idx + 1) % 6][1])
ans = ((w*h) - (subw*subh)) * k
print(ans)
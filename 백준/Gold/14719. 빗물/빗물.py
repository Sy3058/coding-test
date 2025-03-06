import sys
input = sys.stdin.readline

h, w = map(int, input().split())
wall = list(map(int, input().split()))

ans = 0
for i in range (1, w-1): # 어차피 양 끝은 블럭이 있든 없든 물이 찰 수 없음
  l = max(wall[:i]) # 현재 위치를 기준으로 왼쪽에 있는 블럭 중 높이가 가장 높은 블럭
  r = max(wall[i+1:]) # 오른쪽에 있는 블럭 중 높이가 가장 높은 블럭
  rain = min(l, r) # 둘 중 낮은 블럭의 높이만큼 빗물이 찰 수 있음

  if rain > wall[i]: # 현재 위치의 높이보다 빗물의 높이가 높아야 빗물이 고임
    ans += rain - wall[i]

print(ans)
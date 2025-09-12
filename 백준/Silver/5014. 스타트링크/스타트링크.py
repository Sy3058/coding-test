from collections import deque
import sys
input = sys.stdin.readline

"""
f: 건물의 총 층 수
s: 강호의 현 위치
g: 스타트링크의 층 수 (타겟)
u: 위로 u만큼 이동
d: 아래로 d만큼 이동
"""

f, s, g, u, d = map(int, input().split())
cnt = [0] * (f+1) # 방문할 수 있는 모든 층

def bfs():  
    queue = deque()  
    queue.append(s)

    cnt[s] = 1

    while queue:  
        y = queue.popleft()  

        if y == g: # 목표에 도달한 경우 횟수 출력
            return cnt[y] - 1 # cnt[y] 아님 주의!
        else:  
            for x in (y + u, y - d):  
                # 범위 내이고 방문된 적 없을 때 (최단거리)
                if (0 < x <= f) and cnt[x] == 0:  
                    cnt[x] = cnt[y] + 1  
                    queue.append(x)  

    # 끝까지 목표에 도달할 수 없는 경우
    return "use the stairs"  


print(bfs())
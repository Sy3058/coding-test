import heapq
"""
세로 n 가로 m board[n][m]
시추관은 수직은 하나만 (열 하나를 관통)
열마다 덩어리를 추가 (1:[8], 2:[8], 3:[8], 4:[7], 5:[7] 6:[7]: 7:[7, 2], 8:[2])와 같은 식
"""
def solution(land):
    deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    n = len(land)
    m = len(land[0])
    def dfs(r, c, visited, visited_column):
        nonlocal cnt # 석유 덩어리의 크기
        need_visited = [(r, c)]
        
        while need_visited: # 방문해야할 곳이 하나라도 있을 때
            x, y = need_visited.pop()
            
            for dx, dy in deltas:
                nx, ny = x + dx, y + dy
                
                if not (0 <= nx < n and 0 <= ny < m): # 땅을 벗어나면 다음으로
                    continue
                
                if visited[nx][ny]: # 이미 방문된 적 있으면 다음으로
                    continue
                    
                if land[nx][ny] == 0: # 석유가 묻혀있지 않다면 다음으로
                    continue
                
                # 모든 조건을 만족한다면 다음 방문 예정지에 추가
                need_visited.append((nx, ny))
                visited[nx][ny] = True
                visited_column.add(ny)
                cnt += 1
        return (cnt, visited_column)
    
    visited = [[False] * m for _ in range (n)] # 방문해야할 땅
    total = {i:0 for i in range (m)} # 열 별 석유량 총합
    for r in range (n):
        for c in range (m):
            if land[r][c] == 1 and not visited[r][c]:
                visited_column = set([c])
                visited[r][c] = True
                cnt = 1
                cnt, visited_column = dfs(r, c, visited, visited_column)
                for column in visited_column:
                    total[column] += cnt
    return max(total.values())
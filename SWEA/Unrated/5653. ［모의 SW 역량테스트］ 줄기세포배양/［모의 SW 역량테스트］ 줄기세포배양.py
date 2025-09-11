deltas = ((1, 0), (-1, 0), (0, 1), (0, -1)) # 이동 방향

class Cell:
  def __init__(self, life):
    self.life = life
    self.state = 'inactive' # inactive, active, dead 중 하나
    self.time = 0 # 경과한 시간

for tc in range (1, int(input()) + 1):
  n, m, k = map(int, input().split()) # 세로 크기, 가로 크기, 배양 시간
  grid = [list(map(int, input().split())) for _ in range (n)]
  cell_pos = dict()

  for i in range (n):
    for j in range (m):
      if grid[i][j] != 0:
        cell_pos[(i, j)] = Cell(grid[i][j])
  
  for t in range (k): # 매 시간 반복
    next_gen = dict() # 이번에 번식할 세포
    temp_list = [] # 모든 번식할 위치와 생명력을 저장할 임시 리스트
    for pos, c in cell_pos.items():
      c.time += 1
      # cell이 비활성 상태라면
      if c.state == 'inactive':
        # 경과 시간(time)이 life면 활성 상태로 변경
        if c.time == c.life:
          c.state = 'active'
      
      # 활성 상태라면
      elif c.state == 'active':
        # 활성상태가 되고 1초가 경과했다면 번식
        if c.time == c.life + 1:
          for dx, dy in deltas:
            nx, ny = pos[0] + dx, pos[1] + dy
            # cell_pos에 없는 경우에만 추가
            if (nx, ny) not in cell_pos:
              temp_list.append((nx, ny, c.life)) # 임시 리스트에 저장
        
        # 경과 시간이 life * 2이면 cell 죽이기
        if c.time == 2 * c.life:
          c.state = 'dead'
    
    # 번식시키기
    temp_list.sort(key = lambda x:x[2]) # 생명력 오름차순으로 정렬
    for r, c, life in temp_list:
      # 오름차순이므로 마지막으로 갱신되는 값이 가장 큰 값
      next_gen[(r, c)] = Cell(life)
    
    # 딕셔너리 병합시키기
    cell_pos.update(next_gen)
  
  cnt = 0
  for pos, c in cell_pos.items():
    if c.state != 'dead':
      cnt += 1
  print(f"#{tc} {cnt}")
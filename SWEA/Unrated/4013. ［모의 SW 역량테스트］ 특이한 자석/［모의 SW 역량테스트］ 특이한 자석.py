from collections import deque

def rotate(idx, dir):
  nr = set([(idx, dir)]) # 돌려야하는 자석 저장 (idx, dir)
  # 오른쪽으로 진행
  for i in range (idx, 3):
    # 타겟의 2번과 다음 자석의 6번이 동일하면 타겟만 회전
    if m_blade[i][2] == m_blade[i+1][6]:
      # 앞이 안 돌아가면 뒤도 돌아가지 않음
      break
    else:
      if (i - idx) % 2 == 0:
        nr.add((i+1, -dir))
      else:
        nr.add((i+1, dir))

  # 왼쪽으로 진행
  for i in range (idx, 0, -1):
    if m_blade[i][6] == m_blade[i-1][2]:
      # 앞이 안 돌아가면 뒤도 돌아가지 않음
      break
    else:
      if (idx - i) % 2 == 0:
        nr.add((i-1, -dir))
      else:
        nr.add((i-1, dir))
  # 돌려야 하는 자석 돌리기
  for (i, d) in nr:
    m_blade[i].rotate(d)

for tc in range (1, int(input()) + 1):
  k = int(input()) # 자석 회전 횟수
  m_blade = [] # 자석 별 자성 정보
  total_score = 0 # 전체 점수
  for _ in range (4):
    # 8개 날의 자성 정보
    blade = deque(map(int, input().split()))
    m_blade.append(blade)
  
  for _ in range (k):
    # 회전 정보
    mnum, dir = map(int, input().split())
    rotate(mnum-1, dir)

  score = 0
  for i in range (4):
    if m_blade[i][0] == 1:
      total_score += (1 << i)
  print(f"#{tc} {total_score}")
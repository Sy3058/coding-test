standard_input="""5 0 0 3 0 2 2 0 3 0 0 5 4 0 1 1 0 4
4 1 0 3 0 2 4 1 0 1 1 3 0 0 5 1 1 3
5 0 0 4 0 1 2 2 1 2 0 3 1 0 4 0 0 5
5 0 0 3 1 1 2 1 2 2 0 3 0 0 5 1 0 4
"""
results = [list(map(int, input().split())) for _ in range (4)]
countries = ["A", "B", "C", "D", "E", "F"]

def make_combination():
  combs = []
  # A, B, C, D, E, F가 경기를 할 때 가능한 조합 (A-B, B-A는 동일)
  for i in range (6):
    for j in range (i+1, 6):
      combs.append((countries[i], countries[j]))
  return combs

combinations = make_combination()

def possible(target):
  goal = {}
  for i, c in enumerate(countries):
    goal[c] = target[i*3:(i + 1) * 3] # 입력된 결과의 [승, 무, 패] * 6을 나라:[승, 무, 패] 형태로 저장
  
  current = {c: [0, 0, 0] for c in countries} # 현재 결과
  flag = False

  def backtrack(idx):
    nonlocal flag
    if flag: # 이미 불가능한 경우라면 중단
      return
    
    if idx == len(combinations): # 모든 조합을 다 탐색했다면 중단
      # 목표와 현재 결과 비교
      for c in countries:
        if current[c] != goal[c]: # 현재 목표와 타겟이 다르다면 다음 탐색
          return
      flag = True # 앞에서 걸러지지 않았다면 타겟과 동일한 것
      return
    
    c1, c2 = combinations[idx]

    # 1. c1 승, c2 패
    current[c1][0] += 1
    current[c2][2] += 1
    if current[c1][0] <= goal[c1][0] and current[c2][2] <= goal[c2][2]: # current가 goal보다 커지면 불가능하므로 굳이 탐색할 필요없음
      backtrack(idx + 1)
    current[c1][0] -= 1
    current[c2][2] -= 1
    
    # 2. 무승부
    current[c1][1] += 1
    current[c2][1] += 1
    if current[c1][1] <= goal[c1][1] and current[c2][1] <= goal[c2][1]:
      backtrack(idx + 1)
    current[c1][1] -= 1
    current[c2][1] -= 1
    
    # 3. c1 패, c2 승
    current[c1][2] += 1
    current[c2][0] += 1
    if current[c1][2] <= goal[c1][2] and current[c2][0] <= goal[c2][0]:
      backtrack(idx + 1)
    current[c1][2] -= 1
    current[c2][0] -= 1    
  
  backtrack(0)
  return flag

answer = []
for r in results:
  answer.append(1 if possible(r) else 0)

print(*answer)
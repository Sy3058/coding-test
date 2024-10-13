colors, nums = [], []
score = 0

for _ in range (5):
  color, num = input().split()
  colors.append(color)
  nums.append(int(num))

color_list = list(set(colors))
num_list = list(set(nums))
num_list.sort()
cnts = []
pairs = [] # 2장 2장일 때 확인

for n in num_list:
  cnt = nums.count(n)
  cnts.append(cnt)

if len(color_list) == 1: # 색이 모두 동일
  if max(nums) - min(nums) == 4 and len(num_list) == 5: # 색 동일, 연속 숫자
    score = 900 + max(nums)
  else: # 색 동일, 비연속 숫자
    score = 600 + max(nums)

elif len(num_list) == 2:
  if 4 in cnts: # 4장 동일
    score = 800 + num_list[cnts.index(4)]
  else: # 3장 2장 동일
    score = 700 + 10 * num_list[cnts.index(3)] + num_list[cnts.index(2)]

elif len(num_list) == 3:
  if 3 in cnts: # 3장 동일
    score = 400 + num_list[cnts.index(3)]
  else: # 2장 2장 동일
    for i in range (3):
      if cnts[i] == 2:
        pairs.append(num_list[i])
    score = 300 + 10 * max(pairs) + min(pairs)

elif len(cnts) == 4: # 2장만 동일
  score = 200 + num_list[cnts.index(2)]

elif len(num_list) == 5:
  if max(nums) - min(nums) == 4 and len(num_list) == 5:
    score = 500 + max(nums)
  else:
    score = 100 + max(nums)

print(score)
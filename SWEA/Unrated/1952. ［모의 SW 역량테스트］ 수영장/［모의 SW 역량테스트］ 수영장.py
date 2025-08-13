for tc in range (1, int(input()) + 1):
  od, om, tm, oy = map(int, input().split()) # oneDay oneMonth threeMonth oneYear
  up = list(map(int, input().split())) # usagePlan

  price = [0] * 12
  for i in range (12): # 기본 값 배정
    price[i] = up[i] * od
    if price[i] > om:
      price[i] = om

  def backtrack(month, cost):
    global min_cost
    if month >= 12: # 인덱스가 0부터 시작하므로 12 이상으로 비교
      min_cost = min(min_cost, cost)
      return

    # 한달 값 (1일권 or 1달권 or 0원)
    backtrack(month + 1, cost + price[month])

    # 3개월 이용권
    backtrack(month + 3, cost + tm)

  min_cost = float('inf')
  backtrack(0, 0)
  min_cost = min(min_cost, oy)
  print(f"#{tc} {min_cost}")
import sys
import bisect

N, M = map(int, sys.stdin.readline().split())
options = [] # 칭호
powers = [] # 기준이 되는 값

for _ in range (N):
  option, power = sys.stdin.readline().split()
  power = int(power)
  if len(powers) == 0 or power > powers[-1]: # power == powers[-1]인 경우에는 추가하지 않음
    options.append(option)
    powers.append(power)

# bisect_left(array, x): 정렬된 순서를 유지하면서 array에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
for _ in range (M):
  p = int(sys.stdin.readline())
  idx = bisect.bisect_left(powers, p)
  print(options[idx])
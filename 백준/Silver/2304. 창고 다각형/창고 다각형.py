import sys

# 입력 처리
n = int(sys.stdin.readline())  # 기둥의 개수
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 위치 기준으로 정렬
arr.sort(key=lambda x: x[0])

# 최대 높이와 해당 기둥 찾기
max_height = max(arr, key=lambda x: x[1])[1]
max_indices = [i for i, val in enumerate(arr) if val[1] == max_height]
first_max_idx = max_indices[0]
last_max_idx = max_indices[-1]

# 왼쪽에서 최대 높이까지 면적 계산
current_height = 0
last_position = arr[0][0]
area = 0

for i in range(first_max_idx + 1):
    position, height = arr[i]
    if height > current_height:
        area += current_height * (position - last_position)
        current_height = height
        last_position = position

# 오른쪽에서 최대 높이까지 면적 계산
current_height = 0
last_position = arr[-1][0]

for i in range(len(arr) - 1, last_max_idx - 1, -1):
    position, height = arr[i]
    if height > current_height:
        area += current_height * (last_position - position)
        current_height = height
        last_position = position

# 최대 높이 구간 면적 추가
area += max_height * (arr[last_max_idx][0] - arr[first_max_idx][0] + 1)

# 결과 출력
print(area)

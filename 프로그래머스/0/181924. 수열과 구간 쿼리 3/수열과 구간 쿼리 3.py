def solution(arr, queries):
    for i in queries:
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    return arr

# 리스트의 i번째 요소와 j번째 요소의 값을 변경하려면 arr[i], arr[j] = arr[j], arr[i] 하면 됨

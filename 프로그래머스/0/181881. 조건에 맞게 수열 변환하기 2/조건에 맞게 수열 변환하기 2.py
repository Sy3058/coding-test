def solution(arr):
    answer = 0
    while min(arr) % 2 != 1:
        arr.remove(min(arr))
        if len(arr) == 0:
            return 0
    check = min(arr)
    while check < 50:
        check = check*2 + 1
        answer += 1
    return answer
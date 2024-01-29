def solution(arr):
    for i in range (0, 11):
        if len(arr) <= 2 ** i:
            while len(arr) < 2 ** i:
                arr.append(0)
            break
    return arr
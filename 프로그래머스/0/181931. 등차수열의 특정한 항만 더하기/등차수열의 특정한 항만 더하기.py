def solution(a, d, included):
    res = a
    result = 0
    for i in included:
        if i == True:
            result += res
        res += d
    return result
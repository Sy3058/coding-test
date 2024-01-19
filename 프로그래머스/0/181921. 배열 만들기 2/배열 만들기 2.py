def solution(l, r):
    result = []
    out = set(['1','2','3','4','6','7','8','9'])
    for i in range (l, r+1, 1):
        si = set(str(i))
        if not si & out:
            result.append(i)
    if result == []:
        return [-1]
    return result
        
def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        num = list(i)
        check = int(''.join(num[s:s+l]))
        if check > k:
            answer.append(check)
    return answer
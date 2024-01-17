def solution(a, b):
    result_a = int(str(a)+str(b))
    result_b = 2*a*b
    answer = max(result_a, result_b)
    return answer
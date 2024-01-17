def solution(a, b):
    result_a = int(str(a)+str(b))
    result_b = int(str(b)+str(a))
    if result_a >= result_b:
        answer = result_a
    else:
        answer = result_b
    return answer
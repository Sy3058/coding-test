def solution(my_string, n):
    strlist = list(my_string)
    answer = strlist[-n:]
    return ''.join(answer)
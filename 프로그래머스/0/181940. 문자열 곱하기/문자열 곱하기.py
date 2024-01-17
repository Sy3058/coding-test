def solution(my_string, k):
    a_list = []
    for i in range(0, k, 1):
        a_list.append(my_string)
    answer = ''.join(a_list)
    return answer
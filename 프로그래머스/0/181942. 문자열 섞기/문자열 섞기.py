def solution(str1, str2):
    a_list = list(str1)
    b_list = list(str2)
    c_list = []
    for i in range (len(a_list)):
        c_list.append(a_list[i])
        c_list.append(b_list[i])
    answer = ''.join(c_list)
    return answer
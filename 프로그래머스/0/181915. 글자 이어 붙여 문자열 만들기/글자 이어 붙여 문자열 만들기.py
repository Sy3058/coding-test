def solution(my_string, index_list):
    strlist = list(my_string)
    answer = []
    for i in index_list:
        answer.append(strlist[i])
    return ''.join(answer)
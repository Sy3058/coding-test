def solution(my_strings, parts):
    answer = []
    for i in range (len(my_strings)):
        str_list = list(my_strings[i])
        for j in range (parts[i][0], parts[i][1]+1):
            answer.append(str_list[j])
    return ''.join(answer)
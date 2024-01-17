def solution(my_string, overwrite_string, s):
    my_list = list(my_string)
    over_list = list(overwrite_string)
    o_range = len(over_list)
    for i in range (s, o_range+s, 1):
        my_list[i] = over_list[i-s]
    answer = ''.join(my_list)
    return answer
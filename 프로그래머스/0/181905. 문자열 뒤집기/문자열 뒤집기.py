def solution(my_string, s, e):
    my_string = list(my_string)
    rs = list(reversed(my_string))
    if s == 0:
        my_string[s:e+1] = rs[-(e+1):]
    else:
        my_string[s:e+1] = rs[-(e+1):-s]
    return ''.join(my_string)
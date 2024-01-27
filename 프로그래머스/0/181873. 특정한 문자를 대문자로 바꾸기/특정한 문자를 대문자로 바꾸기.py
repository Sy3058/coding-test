def solution(my_string, alp):
    my_string = my_string.lower()
    my_string = my_string.replace(alp, alp.upper())
    return my_string
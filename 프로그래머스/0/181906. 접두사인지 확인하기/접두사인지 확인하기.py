def solution(my_string, is_prefix):
    prefix = []
    my_string = list(my_string)
    for i in range (len(my_string)):
        prefix.append(''.join(my_string[:i+1]))
    if is_prefix in prefix:
        return 1
    else:
        return 0
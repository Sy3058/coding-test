def solution(my_string, queries):
    my_string = list(my_string)
    for query in queries:
        change = my_string[query[0]:query[1]+1]
        my_string[query[0]:query[1]+1] = list(reversed(change))
    return ''.join(my_string)
def solution(code):
    mode = 0
    idx = 0
    ret = ''
    code = list(code)
    test = []
    for i in code:
        if mode == 0:
            if code[idx] == '1':
                mode = 1
            elif code[idx] != '1' and idx%2 == 0:
                ret += code[idx]
        elif mode == 1:
            if code[idx] == '1':
                mode = 0
            elif code[idx] != '1' and idx%2 == 1:
                ret += code[idx]
        idx += 1
    if ret == '':
        ret = 'EMPTY'
    return ret
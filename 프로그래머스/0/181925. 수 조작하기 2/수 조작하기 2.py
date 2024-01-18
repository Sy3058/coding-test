def solution(numLog):
    result = ''
    c = {1:'w', -1:'s', 10:'d', -10:'a'}
    for i in range (len(numLog)-1):
        result+=c[numLog[i+1]-numLog[i]]
    return result
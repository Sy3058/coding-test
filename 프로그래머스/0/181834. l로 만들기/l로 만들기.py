def solution(myString):
    ch = ['a','b','c','d','e','f','g','h','i','j','k']
    answer = ''
    for i in myString:
        if i not in ch:
            answer += i
        else:
            answer += 'l'
    return answer
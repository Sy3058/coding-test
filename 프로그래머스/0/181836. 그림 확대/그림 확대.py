def solution(picture, k):
    answer = []
    for i in picture:
        piece = ''
        for j in i:
            piece += k*j
        for l in range (k):
            answer.append(piece)
    return answer
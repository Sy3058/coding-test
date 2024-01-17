def solution(n):
    answer = 0
    if n%2 == 1:
        return ((n+1)//2)**2
    else:
        for i in range (1, n//2+1, 1):
            answer += i**2
        return answer*4
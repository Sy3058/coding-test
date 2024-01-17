def solution(num_list):
    mul = 1
    sq = 0
    for i in num_list:
        mul *= i
        sq += i
    if mul<sq**2:
        return 1
    else:
        return 0
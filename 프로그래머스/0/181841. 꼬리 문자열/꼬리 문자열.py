def solution(str_list, ex):
    ans = ''
    for i in str_list:
        if ex not in i:
            ans += i
    return ans
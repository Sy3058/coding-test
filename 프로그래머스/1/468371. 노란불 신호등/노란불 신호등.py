def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(signals):
    periods = [g + y + r for g, y, r in signals]
    
    # 최대 공배수를 넘어가면 노란불이 되는 경우가 존재하지 않으므로 limit 구하기
    limit = 1
    for p in periods:
        limit = limit * p // gcd(limit, p)
    
    for t in range (1, limit + 1):
        all_y = True
        
        for i in range (len(signals)):
            g, y, r = signals[i]
            pos = (t - 1) % periods[i]
            
            if not (g <= pos < g + y): # 노란불인 조건
                all_y = False
                break
        
        if all_y:
            return t
    
    return -1
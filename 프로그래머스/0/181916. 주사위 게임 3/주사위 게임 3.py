def solution(a, b, c, d):
    nl = [a,b,c,d]
    nl = sorted(nl)
    if nl[0] == nl[3]:
        return nl[0]*1111
    elif nl[0] == nl[2]:
        return (10*nl[0]+nl[3])**2
    elif nl[1] == nl[3]:
        return (10*nl[3]+nl[0])**2
    elif nl[0] == nl[1] and nl[2] == nl[3]:
        return nl[3]**2 - nl[0]**2
    elif nl[0] == nl[1]:
        return nl[2]*nl[3]
    elif nl[1] == nl[2]:
        return nl[0]*nl[3]
    elif nl[2] == nl[3]:
        return nl[0]*nl[1]
    else:
        return nl[0]
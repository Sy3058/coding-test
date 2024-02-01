def solution(date1, date2):
    date1 = [str(i) for i in date1]
    date2 = [str(i) for i in date2]
    for i in range (len(date1)):
        if len(date1[i]) == 1:
            date1[i] = '0'+date1[i]
        if len(date2[i]) == 1:
            date2[i] = '0'+date2[i]
    if int(''.join(date1) < ''.join(date2)):
        return 1
    else:
        return 0
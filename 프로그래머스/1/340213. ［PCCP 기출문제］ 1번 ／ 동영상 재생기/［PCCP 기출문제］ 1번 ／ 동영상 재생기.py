def solution(video_len, pos, op_start, op_end, commands):
    def change_s(time): # change to second
        m, s = map(int,time.split(':'))
        return m*60 + s
    def change_m(time): # change to minute
        m = time//60
        s = time%60
        return ('%02d:%02d'%(m,s))
        
    
    vl = change_s(video_len)
    cur_time = change_s(pos)
    os = change_s(op_start)
    oe = change_s(op_end)
    
    def check_op(time, os, oe): # check if time is in opening
        if os <= time < oe:
            time = oe
        return time
    
    cur_time = check_op(cur_time, os, oe)
    for c in commands:
        if c == "next":
            cur_time += 10
            if cur_time > vl:
                cur_time = vl
        else:
            cur_time -= 10
            if cur_time < 0:
                cur_time = 0
        cur_time = check_op(cur_time, os, oe)
    
    answer = change_m(cur_time)
    return answer
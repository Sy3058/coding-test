def solution(num_list):
    ln = len(num_list)-1
    if num_list[ln] > num_list[ln-1]:
        num_list.append(num_list[ln]-num_list[ln-1])
    else:
        num_list.append(num_list[ln]*2)
    return num_list
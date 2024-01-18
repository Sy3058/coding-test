'''
첫 풀이
def solution(num_list):
    ln = len(num_list)-1
    if num_list[ln] > num_list[ln-1]:
        num_list.append(num_list[ln]-num_list[ln-1])
    else:
        num_list.append(num_list[ln]*2)
    return num_list
'''
def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1]-num_list[-2])
    else:
        num_list.append(num_list[-1]*2)
    return num_list
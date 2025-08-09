"""
체력회복불가: 최대체력일때 / 체력이 0 이하일 때
붕대 감기: 1초당 x만큼 t초동안 체력 회복 -> t초 모두 회복시 y만큼 추가 회복
공격당하거나 기술이 끝나면 즉시 붕대 감기 다시 사용 (t = 0 초기화)
체력이 0이 되면 바로 -1 리턴
bandage [시전 시간, 초당 회복량, 추가 회복량] (t, x, y)
attacks [공격 시간, 피해량]
초기 상태: health (최대 체력)
"""
def solution(bandage, health, attacks):
    
    time = 0 # 현재 시간
    bandage_time = 0 # 연속 성공 시간
    cur_health = health # 현재 체력
    idx = 0 # 몇번째 공격인지 확인
    while time <= attacks[-1][0]: # 마지막으로 공격할 때까지 확인
        if time == attacks[idx][0]: # 공격하는 턴일 때
            bandage_time = 0 # 연속 성공 시간 초기화
            cur_health -= attacks[idx][1]
            idx += 1
            
            if cur_health <= 0:
                return -1
            
        else: # 공격하지 않을 때
            bandage_time += 1 # 연속 성공 시간 추가
            cur_health += bandage[1] # 체력 회복
            if bandage_time == bandage[0]: # 끝까지 스킬을 사용한 경우
                cur_health += bandage[2] # y만큼 추가체력 회복
                bandage_time = 0 # 연속 성공 시간 초기화
            
            if cur_health > health:
                cur_health = health # 최대 체력까지만 회복 가능
        
        print(time, cur_health)
        time += 1      
        
    return cur_health
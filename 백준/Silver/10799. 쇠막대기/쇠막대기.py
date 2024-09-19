arr = input()
arr_ch = arr.replace('()', '+')  # 레이저를 '+'로 변환

answer = 0  # 최종 결과값 (잘린 쇠막대기 조각 수)
stack = []  # 열린 괄호 '('를 저장할 스택

# 배열을 순회하면서 괄호와 레이저 처리
for i in range(len(arr_ch)):
    if arr_ch[i] == '(':  # 열린 괄호: 쇠막대기 시작
        stack.append('(')  # 스택에 추가
    elif arr_ch[i] == '+':  # 레이저: 현재 스택에 있는 열린 괄호만큼 쇠막대기가 잘림
        answer += len(stack)  # 스택의 길이 = 열린 괄호의 수 = 잘리는 쇠막대기의 수
    elif arr_ch[i] == ')':  # 닫힌 괄호: 쇠막대기 끝남
        stack.pop()  # 열린 괄호 하나 닫힘
        answer += 1  # 쇠막대기의 끝이므로 잘린 조각 하나 추가

print(answer)
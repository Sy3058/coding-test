# [D3] 규영이와 인영이의 카드게임 - 6808 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWgv9va6HnkDFAW0) 

### 성능 요약

메모리: 30,032 KB, 시간: 2,462 ms, 코드길이: 1,776 Bytes

### 제출 일자

2025-09-08 09:27

### 🔎 접근 과정

> 문제 해결을 위한 접근 방식을 설명해주세요.

- 🔹 **어떤 알고리즘을 사용했는지**
백트래킹

- 🔹 **어떤 방식으로 접근했는지**
백트래킹을 이용해 인영이의 카드 조합 순열을 생성하고 해당 순열을 사용할 때 승패를 계산

### ⏱️ 시간 복잡도

> **시간 복잡도 분석을 작성해주세요.**  
> 최악의 경우 수행 시간은 어느 정도인지 분석합니다.

- **Big-O 표기법:** `O(1)`
- **이유:**
permutation이 9!만큼 돌아감. 상수에 해당하므로 O(1)

> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do
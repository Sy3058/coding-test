function solution(people, limit) {
    var answer = 0;
    people.sort((a, b) => (b - a)); // 내림차순
    // 이진탐색으로 가능한 가장 무거운 사람과 가장 가벼운 사람 매치 (몸무게 합 최소)
    let left = 0;
    let right = people.length - 1;
    
    while (left <= right) {
        // 구명보트의 무게제한보다 몸무게가 적으면 하나에 두 명 태울 수 있음
        if (people[left] + people[right] <= limit) {
            answer++;
            left++;
            right--;
        } else {
            answer++; // 무거운 사람은 혼자 태워야함
            left++; // 무거운 사람의 무게가 줄어드는 방향으로 가야함
        }
    }
    return answer;
}
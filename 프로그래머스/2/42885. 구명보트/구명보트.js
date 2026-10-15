function solution(people, limit) {
    var answer = 0;
    people.sort((a, b) => (b - a)); // 내림차순
    // 이진탐색으로 가능한 가장 무거운 사람과 가장 가벼운 사람 매치 (몸무게 합 최소)
    let left = 0;
    let right = people.length - 1;
    
    while (left <= right) {
        // 가벼운 사람도 함께 태울 수 있으면 태우고 출발
        if (left < right && people[left] + people[right] <= limit) {
            right--;
        }
        
        // 어떤 경우에도 무거운 사람은 보트를 타고 출발함
        answer++;
        left++;
    }
    return answer;
}
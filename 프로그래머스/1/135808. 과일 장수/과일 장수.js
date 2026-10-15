function solution(k, m, score) {
    let answer = 0;
    
    score.sort((a, b) => b - a); // 내림차순
    
    n = score.length;
    
    // 상자에 들어가는 사과의 수보다 사과 개수가 적으면 팔 수 없음
    if (n < m) {
        return 0;
    }
    
    for (let i = m; i <= n; i += m) {
        answer += m * score[i - 1];
    }
    
    return answer;
}
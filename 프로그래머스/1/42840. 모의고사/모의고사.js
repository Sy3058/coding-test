function solution(answers) {
    var answer = [];
    const s1 = [1, 2, 3, 4, 5]
    const s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    const s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    let s1A = 0;
    let s2A = 0;
    let s3A = 0;
    
    for (let i = 0; i < answers.length; i++) {
        if (answers[i] == s1[i % s1.length]) {
            s1A++
        }
        if (answers[i] == s2[i % s2.length]) {
            s2A++
        }
        if (answers[i] == s3[i % s3.length]) {
            s3A++
        }
    }
    
    const maxA = Math.max(s1A, s2A, s3A);
    
    if (maxA == s1A) {answer.push(1)};
    if (maxA == s2A) {answer.push(2)};
    if (maxA == s3A) {answer.push(3)};
    
    return answer;
}
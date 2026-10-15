function solution(arr) {
    var answer = [arr[0]];

    for (const num of arr) {
        if (answer[answer.length - 1] != num) {
            answer.push(num);
        }
    }

    return answer;
}
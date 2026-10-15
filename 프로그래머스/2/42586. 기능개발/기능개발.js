function solution(progresses, speeds) {
    var answer = [];
    
    const needDate = [];
    
    for (let i = 0; i < progresses.length; i++) {
        needDate.push(Math.ceil((100 - progresses[i]) / speeds[i]))
    }
    console.log(needDate);
    
    let head = 0;
    while (head < progresses.length) {
        let cur = needDate[head++];
        let count = 1;
        while (cur >= needDate[head]) {
            head++
            count++
        }
        answer.push(count)
    }
    
    return answer;
}
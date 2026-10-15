function solution(number, k) {
    const stack = [];
    
    for (const num of number) {
        // 앞에 있는데 현재 수보다 작다면 제거
        while (k > 0 && stack && stack[stack.length - 1] < num) {
            stack.pop();
            k--; // 수를 제거했으므로 k에서 1 빼야 함
        }
        
        stack.push(num);
    }
    
    // 앞에서 제거할 거 다 제거했는데 더 제거해야된다면 뒤에서 순서대로 제거
    while (k > 0) {
        stack.pop();
        k--;
    }
    
    return stack.join('');
}
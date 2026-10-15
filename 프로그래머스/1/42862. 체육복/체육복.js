function solution(n, lost, reserve) {
    const lostSet = new Set(lost);
    const reserveSet = new Set(reserve);

    // 여벌이 있으면서 도난당한 학생은 본인 여벌 사용
    for (const student of lost) {
        if (reserveSet.has(student)) {
            reserveSet.delete(student);
            lostSet.delete(student);
        }
    }

    let imp = 0;

    // 남은 도난 학생을 번호순으로 처리
    const remainingLost = [...lostSet].sort((a, b) => a - b);

    for (const l of remainingLost) {
        if (reserveSet.has(l - 1)) {
            reserveSet.delete(l - 1);
        } else if (reserveSet.has(l + 1)) {
            reserveSet.delete(l + 1);
        } else {
            imp++;
        }
    }

    return n - imp;
}
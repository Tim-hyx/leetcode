/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var fairCandySwap = function (A, B) {
    let sumA = 0;
    let sumB = 0;
    for (let i = 0; i < A.length; i++) {
        sumA += A[i];
    }
    for (let j = 0; j < B.length; j++) {
        sumB += B[j];
    }
    let diff = sumA - sumB // 小于零表示A少于B 大于零表示A多于B
    for (let i = 0; i < A.length; i++) {
        for (let j = 0; j < B.length; j++) {
            if ((A[i] - B[j]) === diff / 2) {
                return [A[i], B[j]]
            }
        }
    }

};

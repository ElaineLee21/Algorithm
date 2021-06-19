// 프로그래머스 - 평균 구하기

// 나의 풀이
function solution(arr) {
    var answer = 0;
    
    let reducer = (acc, cur) => acc + cur;
    let sumOfEls = arr.reduce(reducer);
    answer = sumOfEls / arr.length;

    return answer;
}

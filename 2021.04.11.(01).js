// 프로그래머스 - 자연수 뒤집어 배열로 만들기

// 나의 풀이
function solution(n) {
    var answer = [];

    do{
        answer.push(n%10);
        n = Math.floor(n/10);
    } while(n>0)
    
    return answer;
}

// 다른 사람의 풀이
// 다른 사람들의 풀이를 보니, n을 string화 해서 reverse하는 것이 지배적이었다.
// 하지만 숫자 인자는 숫자인 그대로 연산하는 것이 제일 빠름.
// 고로 나의 풀이가 맘에들어잉

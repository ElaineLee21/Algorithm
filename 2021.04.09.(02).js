// 프로그래머스 - 약수의 합

// 나의 풀이
function solution(n) {
    var answer = 0;
    let arr = [];
    let reducer = (acc, cur) => acc + cur;

// n이 0 또는 1일 경우 굳이 for문을 돌면서 시간복잡도를 높일(?)필요가 없기 때문에 따로 빼줌
// 근데 굳이 이렇게 분리시켰어야 하는 생각은 든다.
// 확실히 if (n===0)은 필요함. 근데 if (n===1)은 민 아래 else if문으로도 해결 가능.

    if (n === 0) {
      answer = 0;
    }
		else if (n === 1) {
      answer = 1;
    }
		else if (n > 1) {
      for (let i = 1; i <= n; i++) {
        if (n % i === 0) {
          arr.push(i);
        }
      }
      answer = arr.reduce(reducer);
    }

    return answer;
}

// 다른 사람의 풀이
function solution(n) {
    let sum = 0;
    for (let i = 1; i <= n; i++) {
        if (n % i === 0) {
		sum += i
	}
    }
    return sum;
}

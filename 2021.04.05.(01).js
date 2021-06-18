// 프로그래머스 - 문자열을 정수로 바꾸기

// 나의 풀이
function solution(s) {
   var answer = 0;
   answer = Number(s);
   return answer;
}

// 다른 사람의 풀이
function solution(s){
	var answer = 0;
   answer = s / 1;
	return answer;
  }

// Tip
// 숫자로 이루어진 string은 나눗셈, 곱셈을 할 경우 숫자로 parsing된다.

var string2 = '2'

string2 / 1;
// 2

string2 * 2;
// 4
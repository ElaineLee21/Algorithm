// 프로그래머스 - 두 정수 사이의 합

// 나의 풀이
function solution(a, b) {
   var answer = 0;

// a가 3, b가 1일 경우
   var numArr = [a, b];
   var sortedNumArr = numArr.sort(); // [1, 3]
   var firstNum = sortedNumArr[0]; // 1
   var secondNum = sortedNumArr[1]; // 3

   if (firstNum < 0 && secondNum < 0) {
     while (secondNum <= firstNum) {
       answer = answer + secondNum;
       secondNum += 1;
     }
   } else {
     while (firstNum <= secondNum) { 
       answer = answer + firstNum;
       firstNum += 1;
     }
   }
   
   return answer;
}

// 다른 사람의 풀이
function adder(a, b){
   return (a+b)*(Math.abs(b-a)+1)/2;
}

// a = 1, b = 5라면
// Math.abs(b-1)+1 / 2 는 6이 총 몇 개 있는지 알아내는 메소드.
// 1+2+3+4+5는 6이 몇 개 있는지 알아내고 더한 후, 가운데 수인 6의 1/2를 더하면 되기 때문.
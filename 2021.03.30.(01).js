// 프로그래머스 - 나누어 떨어지는 숫자 배열

// 나의 풀이
function solution(arr, divisor) {
   let answer = [];
   arr.sort(function(a, b){return a-b});

   for(let i = 0; i < arr.length; i++){
       if(arr[i]%divisor === 0)    answer.push(arr[i]);
   }

   if(answer.length === 0) answer.push(-1);

   return answer;
}

// 다른 사람의 풀이
function solution(arr, divisor) {
   var answer = arr.filter(v => v%divisor == 0);
   return answer.length == 0 ? [-1] : answer.sort((a,b) => a-b);
}
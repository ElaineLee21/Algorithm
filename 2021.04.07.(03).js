// 프로그래머스 - 같은 숫자는 싫어

// 나의 풀이
function solution(arr){
   var answer = []; 
   answer.push(arr[0]);

   for (let i = 1; i < arr.length; i++) {
     if (answer[answer.length-1] !== arr[i]) {
       answer.push(arr[i]);
     }
   }
   return answer;
}

// 다른 사람의 풀이
function solution(arr){
   var answer = [];

   for(var i = 0; i < arr.length; ++i) {
       if(arr[i] != arr[i + 1]) {
              answer.push(arr[i]);
           }
   }
   return answer;
}
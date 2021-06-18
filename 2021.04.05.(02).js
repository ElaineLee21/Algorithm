// 프로그래머스 - 수박수박수박수박수박수?

// 나의 풀이
function solution(n) {
   // 횟수 n번만큼 돌면서 '수' '박'을 차례대로 answer에 concat해야됨
   // answer의 length가 홀수면 '박', 짝수 혹은 0이면 '수'를 concat한다.

   var answer = '';
   
   for (let i = 0; i < n; i++) {
     if (answer.length % 2 === 0) {
       answer = answer.concat('수');
     } else if (answer.length % 2 === 1) {
       answer = answer.concat('박');
     }
   }

   return answer;
}

// 다른 사람의 풀이
function solution(n) {
   var answer = '';
   answer = "수박".repeat(n).slice(0,n);
   return answer;
}
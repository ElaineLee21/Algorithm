// 프로그래머스 -  완주하지 못한 선수

// 나의 풀이
function solution(participant, completion) {
   // arr.sort 하고 participant[i]와 completion[i]가 같은지 확인
   // 다르면 participant[i]를 answer에 재할당
     // 단, 이미 answer에 할당이 된 상태에서는 재할당 X
   var answer = '';
   
   participant.sort();
   completion.sort();
   
   for (let i = 0; i < participant.length; i++) {
       if (participant[i] !== completion[i] && answer.length === 0) {
           answer = participant[i];
       }
   }
   
   return answer;
}

// 다른 사람의 풀이
   participant.find(name=>!completion[name]--,
   completion.map(name=>completion[name]=(completion[name]|0)+1))
   
   // 완주자 배열을 {이름:완주자배열에 등장하는 횟수}로 맵핑하고,
   // 그 맵에 참가자 이름 하나씩 넣어서 찾아볼때마다 횟수 떨어뜨려서 횟수 0나오는 애 찾아뱉는 함수
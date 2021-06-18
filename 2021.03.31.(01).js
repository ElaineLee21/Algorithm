// 프로그래머스 - K번째수

// 나의 풀이
function solution(array, commands) {
   var answer = [];

   // array를 commands[0][0]-1부터 commands[0][1]까지 자른다
   // 오름차순으로 요소 정렬
   // 정렬한 배열의 commands[0][2]를 answer에 push
   // array를 commands[1][0]-1부터 commands[1][1]까지 자른다
   // 오름차순으로 요소 정렬
   // 정렬한 배열의 commands[1][2]를 answer에 push
   // array를 commands[2][0]-1부터 commands[2][1]까지 자른다
   // 오름차순으로 요소 정렬
   // 정렬한 배열의 commands[2][2]를 answer에 push

   for (let i = 0; i < 3; i++) {
     answer.push(
       array.slice(commands[i][0]-1, commands[i][1])
         .sort((a, b) => a - b)[commands[i][2]-1]);
   }

   return answer;
}

// 다른 사람의 풀이
function solution(array, commands) {
   return commands.map(command => {
       const [sPosition, ePosition, position] = command
       const newArray = array
           .filter((value, fIndex) => fIndex >= sPosition - 1 && fIndex <= ePosition - 1)
           .sort((a,b) => a - b)    

       return newArray[position - 1]
   })
}
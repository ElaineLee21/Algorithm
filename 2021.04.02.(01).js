// 프로그래머스 - 가운데 글자 가져오기

// 나의 풀이
function solution(s) {
   var answer = '';
   var position
   var length

   if (s.length % 2 === 1) {
     position = s.length / 2
     length = 1;
   } else {
     position = s.length / 2 - 1
     length = 2;
   }

   answer = s.subString(position, position + length);
   return answer;
}

// 다른 사람의 풀이
function solution(s) {
   return s.substr(Math.ceil(s.length / 2) - 1, s.length % 2 === 0 ? 2 : 1);
}

//Math.ceil은 올림
//ex) Math.ceil(2.5) === 3
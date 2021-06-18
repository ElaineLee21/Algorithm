// 프로그래머스 - 정수 내림차순으로 배치하기

// 나의 풀이
function solution(n) {
   var answer = 0;
 
   //n이 1234라고 쳤을 때
   let arrayOfDigits = Array.from(String(n), Number); //[1,2,3,4]
   answer = arrayOfDigits.sort((a, b) => b - a); //[4,3,2,1]
   answer = answer.map(String); //['4','3','2','1']
   answer = answer.join('') //'4321'
   answer = Number(answer); //4321
 
 return answer;
}

// 다른 사람의 풀이(1)
function solution(n) {

	//n이 2314라고 쳤을 때
  const newN = n + ""; //newN = "2314"
  const newArr = newN //newArr = "2314"
    .split("") //newArr를 2,3,1,4 따로 갖고놀게 됨
    .sort() //newArr = "1,2,3,4"
    .reverse() //newArr = "4,3,2,1"
    .join(""); //newArr = "4321"

  return +newArr; // 아래 설명 참조
}

// Tip
// 단항 연산자 + 를 사용하여 값을 숫자로 변환 할 수도 있습니다:

+ '42';   // 42
+ '010';  // 10
+ '0x10'; // 16

// 다른 사람의 풀이(2) - 숫자로 하는 게 확실히 빠르다.
function solution(n) {
   var nums =[]; 

   //n이 2314라고 쳤을 때
   do{
       nums.push(n%10); //한 바퀴 돌았을 때 nums = [4], n = 2314
   //  ^ 2314를 10으로 나눈 나머지는 4. 즉 1의 자리 숫자를 push하는 method이다
      n=Math.floor(n/10); // n = 231
   //    ^ 2314를 10으로 나눈 231.4를 내림하여 231만 남기는 method
   } while(n>0)
     //다 돌았을 때 nums = [4,1,3,2]

   return nums.sort((a,b)=>b-a).join('')*1;
} //        ^내림차순으로 정렬  ^한 문자열로 합치고 ^number로 형변환
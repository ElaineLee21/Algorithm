// 프로그래머스 - 정수 제곱근 판별

// 나의 풀이
function solution(n) {
    var answer = 0;
    
    let sqrt = Math.sqrt(n)
    if (sqrt % 1 === 0) {
        answer = Math.pow(sqrt+1, 2);
    } else {
        answer = -1;
    }
    
    return answer;
}

// 다른 사람의 풀이
function nextSqaure(n){
  var result = 0;
  var x = 0;
  while (x*x < n){
    x++;
  }
  if (x*x == n){
    x++;
    result = x*x; 
  }else{
    result = 'no';
  }

  return result;
}

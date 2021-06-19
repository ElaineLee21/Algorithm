// 프로그래머스 - 문자열 내 p와 y의 개수

// 나의 풀이
function solution(s){
    var answer = true;
    
  //주어진 문자열 s를 일단 소문자로 통일
    s = s.toLowerCase();
  //arr1에 s를 한글자한글자 push한다
    let arr1 = [];
    for (let i = 0; i < s.length; i++) {
      arr1.push(s[i]);
    }
  //p만으로 이루어진 arrP와 y만으로 이루어진 arrY를 만든다
    let arrP = arr1.filter(letter => letter === 'p');
    let arrY = arr1.filter(letter => letter === 'y');

    if (arrP.length !== arrY.length) {
      answer = false;
    }

    return answer;
}

// 다른 사람의 풀이(1)
function numPY(s){
    return s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length;
}

// 다른 사람의 풀이(2)
function numPY(s) {
  return s.match(/p/ig).length == s.match(/y/ig).length;
}

// 프로그래머스 - 문자열 내 마음대로 정렬하기

// 나의 풀이

function solution(strings, n) {
    strings.sort(function(a,b) {
      let firstStr = a[n];
      let secondStr = b[n];

      if (firstStr === secondStr) {
          return (a>b) - (b>a);
      } else {
          return (firstStr>secondStr) - (secondStr>firstStr);
      }
    })
    return strings;
}

// 다른 사람의 풀이(1)

function solution(strings, n) {
    return strings.sort((s1, s2) => 
						s1[n] === s2[n] ? s1.localeCompare(s2) : s1[n].localeCompare(s2[n]));
}

// 다른 사람의 풀이(2)

function solution(strings, n) {
		return strings.map(a=>[...a][n]+a).sort().map(a=>a.substring(1))
}

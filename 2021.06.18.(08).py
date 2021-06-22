# 백준 11050 하 정수론 및 조합론 - 이항 계수 1

# 내 풀이

'''
- 조합
학생 3명(A,B,C) 중 대표를 2명 뽑는다고 가정하자.
AB, AC, BC 세 가지 경우가 나온다.
이렇게 순서 상관 없이 뽑는 경우를 조합이라고 부르고, 
Combination의 약자를 써서 nCr 이런식으로 나타낸다.

- 순열
학생 3명(A,B,C) 중 반장과 부반장을 한 명씩 뽑는다고 가정하자.
AB, AC, BA, BC, CA, CB 여섯 가지 경우가 나온다.
이렇게 순서가 다른 경우도 고려하여 뽑는 경우를 순열이라고 부르고,
nPr 이런식으로 나타낸다.
'''

n, k = map(int, input().split())

def factorial(n):
   if n <= 1:
      return 1
   return n * factorial(n-1)

print(int(factorial(n) / (factorial(k)*factorial(n-k))))

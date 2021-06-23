# 백준 1010 중 정수론 및 조합론 - 다리 놓기

# 나의 풀이

caseNum = int(input())

def factorial(n):
   if n <= 1:
      return 1
   return n * factorial(n-1)

for i in range(caseNum):
   [a, b] = list(map(int, input().split()))
   n = max([a, b])
   k = min([a, b])
   print(int(factorial(n) / (factorial(k)*factorial(n-k))))

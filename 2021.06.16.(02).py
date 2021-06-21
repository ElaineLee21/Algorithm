# 백준 4948 하 기본 수학 2 - 베르트랑 공준

# 내 풀이(1) (Python3 시간초과, PyPy3 통과)

from math import sqrt

while True:
   n = int(input())
   if n == 0:
      break

   cnt = 0

   # n이 5라면 6,7,8,9,10 돌것.
   for i in range(n+1, 2*n+1):
      if i == 2:
         cnt += 1
         continue
      else: # 6-8까지 j는 2, 9 10은 j는 2 3
         for j in range(2, int(sqrt(i)+1)):
            if i%j == 0:
               break
         else:
            cnt += 1
   print(cnt)

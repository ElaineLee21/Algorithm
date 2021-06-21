# 백준 1011 중 기본 수학 1 - Fly me to the Alpha Centauri

# 내 풀이(코드길이 397B)

from math import sqrt

dist = []

while True:
   try:
      t = int(input())
      break
   except:
      continue

for _ in range(t):
   num1, num2 = input().split()
   dist.append(int(num2)-int(num1))

for dis in dist:
   n = int(sqrt(dis))
   m = n + 1

   if n == 1:
      print(dis)
   elif dis >= n*m+1:
      print(n*2+1)
   elif dis >= n**2+1:
      print(n*2)
   else:
      print(n*2-1)

# 백준 1934 하 정수론 및 조합론 - 최소공배수

# 내 풀이(백준 2609 최대공약수와 최소공배수 풀이를 응용하였음)

n = int(input())

for i in range(n):
   a, b = map(int, input().split())
   divArr = []

   for i in range(2, min(a,b)+1):
      while a%i == 0 and b%i ==0:
         try:
            divArr.append(i)
            a = int(a / i)
            b = int(b / i)         
         except:
            continue

   greatest = 1

   for i in range(len(divArr)):
      greatest = greatest * divArr[i]

   least = greatest * a * b
   print(least)

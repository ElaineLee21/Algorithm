# 백준 9012 중 스택 - 괄호

# 내 풀이

n = int(input())

for i in range(n):
   ps = input()
   psArr = list(ps)
   sum = 0

   for i in psArr:
      if i == '(':
         sum += 1
      elif i == ')':
         sum -= 1
      if sum < 0:
         print('NO')
         break
   if sum > 0:
      print('NO')
   elif sum == 0:
      print('YES')

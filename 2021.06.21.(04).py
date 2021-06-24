# 백준 8958 1차원 배열 - OX퀴즈

# 내 풀이

caseNum = int(input())
for i in range(caseNum):
   result_arr = list(input())
   score = 0
   o = 1
   for i in result_arr:
      if i == 'O':
         score += o
         o += 1
      elif i == 'X':
         o = 1
   print(score)

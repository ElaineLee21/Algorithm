# 백준 11720 문자열 - 숫자의 합

# 내 풀이

n = int(input())
num = list(map(int, input()))
sum = 0

for i in num:
   if i != 0:
      sum += i

print(sum)


# 다른 사람의 풀이

print(sum(map(int,input())))

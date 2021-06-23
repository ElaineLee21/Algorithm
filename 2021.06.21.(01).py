# 백준 2577 1차원 배열 - 숫자의 개수

# 내 풀이

import sys

result = 1

for num in range(3):
   num = int(sys.stdin.readline())
   result = result * num

result = list(str(result))

for i in range(10):
   print(result.count(str(i)))

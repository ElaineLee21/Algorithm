# 백준 10828 하 스택 - 스택

# 내 풀이(1) (python3, pypy3 모두 시간 초과)

n = int(input())
stack = []

for i in range(n):
   order = list(input().split())
   if order[0] == 'push':
      stack.append(order[1])
   elif order[0] == 'pop':
      if len(stack) == 0:
         print(-1)
      else:
         print(stack[len(stack)-1])
         del stack[len(stack)-1]
   elif order[0] == 'size':
      print(len(stack))
   elif order[0] == 'empty':
      if len(stack) == 0:
         print(1)
      else:
         print(0)
   elif order[0] == 'top':
      if len(stack) == 0:
         print(-1)
      else:
         print(stack[len(stack)-1])
          
          
# 해결책
# 이 두 줄을 코드 맨 위에 추가해주었다. 

import sys
input = sys.stdin.readline

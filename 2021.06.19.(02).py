# 백준 18258 하 큐, 덱 - 큐 2

# 나의 풀이

import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())
que = []
count = 0

for i in range(n):
   order = list(input().split())
   if order[0] == 'push':
      que.append(order[1])
   elif order[0] == 'pop':
      if len(que) > count:
         print(que[count])
         count += 1
      else:
         print(-1)
   elif order[0] == 'size':
      print(len(que)-count)
   elif order[0] == 'empty':
      if len(que) == count:
         print(1)
         count = 0
         que = []
      else:
         print(0)
   elif order[0] == 'front':
      if len(que) > count:
         print(que[count])
      else:
         print(-1)
   elif order[0] == 'back':
      if len(que) > count:
         print(que[-1])
      else:
         print(-1)

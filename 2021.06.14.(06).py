# 백준 4673 하 함수 - 셀프 넘버

# 내 풀이

def not_a_self_num(n):
   return n + sum([int(i) for i in str(n)])

arr = [0] * 10000

for i in range(len(arr)):
   if not_a_self_num(i) < 10000:
      arr[not_a_self_num(i)] = 1

for i in range(len(arr)):
   if arr[i] == 0:
      print(i)

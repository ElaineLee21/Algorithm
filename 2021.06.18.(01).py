# 백준 11728 중 재귀 - 하노이 탑 이동 순서

# 내 풀이

n = int(input())

def hanoi(n, start, aux, goal):
   if n == 1:
      print(start, goal)
      return
   hanoi(n-1, start, goal, aux)
   print(start, goal)
   hanoi(n-1, aux, start, goal)

sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
    
print(sum)
hanoi(n, 1, 2, 3)

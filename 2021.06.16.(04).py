# 백준 2869 중하 기본 수학 1 - 달팽이는 올라가고 싶다

# 내 풀이(1) (python3, pypy3 둘다 시간초과)

a, b, v = map(int, input().split())

dis = 0
day = 0

while True:
   dis = dis + a
   day += 1
   if dis >= v:
      print(day)
      break
   if dis != v:
      dis = dis - b

      
# 내 풀이(2)

a, b, v = map(int, input().split())

day = (v-b) / (a-b)

if day == int(day):
   print(int(day))
else:
   print(int(day)+1)

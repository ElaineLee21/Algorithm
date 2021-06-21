# 백준 2839 하 기본 수학 1 - 설탕 배달

# 나의 풀이(코드길이 199B)

sugar = int(input())
bag = 0

while True:
   if sugar % 5 == 0:
      bag = bag + (sugar//5)
      print(bag)
      break
   
   sugar -= 3
   bag += 1

   if sugar < 0:
      print("-1")
      break

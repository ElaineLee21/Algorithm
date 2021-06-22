# 백준 10250 중하 기본 수학 1 - ACM 호텔

# 내 풀이

caseNum = int(input())

for case in range(caseNum):
   h, w, n = map(int, input().split())
   floor = 0
   unit = 1
   while n > h:
      n = n - h
      unit += 1
   floor = n
   print(floor*100 + unit)

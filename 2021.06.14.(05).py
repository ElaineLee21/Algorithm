# 백준 4344 하 1차원 배열 - 평균은 넘겠지

# 내 풀이

# 첫 인풋을 caseNum에 정수형으로 할당
# 빈 배열 avg를 만듦

# for문을 돈다, caseNum만큼.
# 들어오는 인풋을 띄어쓰기를 기준으로 쪼개서, int형으로 맵핑한 결과를 list에 넣는다.
# 0번 인덱스는 학생 수므로 다른 변수에 할당후 지워주고, 배열에 점수만 남게 한다.
# 점수배열을 돌면서, 점수의 총합을 구하고,
# avg에 총합/학생수 하여 점수 평균을 append한다.

# 점수배열을 돌면서, 평균 점수와 비교. 만약 j가 평균을 넘으면 count += 1
# agv[i]에 평균 넘는 학생의 비율을 넣어줌

# for문을 빠져나와 새로운 for문 만들어줌.
# avg에 각 case마다 평균을 넘는 학생의 비율이 써있을 것.
# avg를 돌면서, 소수점 3자리까지 잘라준다. 

caseNum = int(input())
avg = []

for case in range(caseNum):
   scoreArr = list(map(int, input().split()))
   studentNum = scoreArr[0]
   del scoreArr[0]
   sum = 0
   count = 0

   for score in scoreArr:
      sum += score
   avg.append(sum/studentNum)

   for score in scoreArr:
      if avg[case] < score:
         count += 1
   avg[case] = count/studentNum * 100

for case in avg:
   print(f'{case: .3f}%')

# 백준 1546 1차원 배열 - 평균

# 내 풀이

caseNum = int(input())
scores = list(map(int, input().split()))
maxScore = max(scores)
sum = 0

for score in scores:
   score = score / maxScore * 100
   sum = sum + score

print(sum / caseNum)

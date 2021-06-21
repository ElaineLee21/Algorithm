# 백준 1037 하 정수론 및 조합론 - 약수

# 내 풀이

divNum = int(input())
divArr = list(map(int, input().split()))

print(min(divArr)*max(divArr))

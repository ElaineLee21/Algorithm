# 백준 11651 중 정렬 - 좌표 정렬하기 2

# 내 풀이

n = int(input())
numArr= []

for i in range(n):
   [x, y] = map(int, input().split())
   rev = [y, x]
   numArr.append(rev)

sortedNumArr = sorted(numArr)

for i in range(n):
   print(sortedNumArr[i][1], sortedNumArr[i][0])

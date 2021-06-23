# 백준 10818 1차원 배열 - 최소, 최대

# 내 풀이(1)

n = int(input())
numArr = list(map(int, input().split()))
minNum = numArr[0]
maxNum = numArr[0]

for i in numArr:
   if minNum > i:
      minNum = i
   if maxNum < i:
      maxNum = i

print(minNum, maxNum)


# 내 풀이(2)

n = int(input())
numArr = list(map(int, input().split()))
print(min(numArr), max(numArr))

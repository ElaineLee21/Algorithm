# 백준 2562 1차원 배열 - 최댓값

# 내 풀이

numArr = []

for num in range(9):
   num = int(input())
   numArr.append(num)

maxNum = numArr[0]

for num in numArr:
   if maxNum < num:
      maxNum = num

print(maxNum, numArr.index(maxNum)+1, sep='\n')

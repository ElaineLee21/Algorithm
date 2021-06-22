# 백준 2805 중 이분탐색 - 나무 자르기

# 내 풀이(python3 시간초과, pypy3 통과)

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
   cut = (start+end)//2
   log = 0

   for i in tree:
      if i >= cut:
         log += i - cut
   
   if log >= m:
      start = cut+1
   else:
      end = cut-1

print(end)

# 백준 1065 함수 - 한수

# 내 풀이

num = int(input())
count = 0

for i in range(1, num+1):
   if i <= 99:
      count += 1
   
   else:
      num_arr = list(map(int, str(i)))
      if num_arr[1] - num_arr[0] == num_arr[2] - num_arr[1]:
         count += 1

print(count)


# Tip

i = 145

num_arr = list(str(i))
print(num_arr)
# ['1', '4', '5']

num_arr = list(map(int,str(i)))
print(num_arr)
# [1, 4, 5]

# 백준 2908 문자열 - 상수

# 내 풀이

a, b = input().split()
# a = 734, b = 893

a_arr = []
b_arr = []

for i in range(3):
   a_arr.append(a[2-i:3-i])
   b_arr.append(b[2-i:3-i])
	# 첫 번째 돌 때에는 마지막 글자, 두 번째 돌 때에는 그 앞글자 ... 를 빈 배열에 append
# a_arr = ['4','3','7'], b_arr = ['3','9','8']

a = "".join(a_arr)
b = "".join(b_arr)
# a = 437, b = 398

if a > b:
   print(a)
else:
   print(b)
    

# 다른 사람의 풀이

num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else :
    print(num2)

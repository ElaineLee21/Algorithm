# 백준 2588 하하 사칙연산 - 곱셈

# 내 풀이

a = int(input())
b = int(input())

b_one = b % 10
b_ten = (b % 100) - b_one
b_hundred = b - b_ten - b_one

c = a * b_one
d = a * b_ten
e = a * b_hundred

d_result = int(d / 10)
e_result = int(e / 100)
#이렇게 할 필요 없이, 그냥 d 맨뒤에 /10하면 (4)였다..

result = c + d + e
#이렇게 할 필요 없이, a*b한 게 (6)이었다..

print(c)
print(d_result)
print(e_result)
print(result)


# 내 풀이 2(코드길이 220B)

a = int(input())
b = int(input())

b_one = b % 10
b_ten = (b % 100) - b_one
b_hundred = b - b_ten - b_one

c = a * b_one
d = int(a * b_ten /10)
e = int(a * b_hundred /100)
result = a * b

print(c, d, e, result, sep='\n')


# 다른 사람의 풀이(코드길이 158B)

A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠

# 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')
# sep='\n'로 줄바꿈

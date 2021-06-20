# 백준 10869 하하 사칙연산 - 사칙연산

# 내 풀이(코드길이 106B)

a, b = input().split()

a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

# 다른 사람의 풀이(코드길이 73B)

A,B = map(int,input().split())
print(A+B, A-B, A*B, A//B, A%B, sep='\n')	
# sep='\n'로 줄바꿈

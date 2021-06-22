# 백준 10773 하 스택 - 제로

# 내 풀이(시간 3976ms)

n = int(input())
stack = []

for i in range(n):
   num = int(input())
   if num == 0:
      del stack[len(stack)-1]
   else:
      stack.append(num)

result = 0

for i in stack:
   result = result + i

print(result)


# 다른 사람의 풀이(시간 4020ms)

n = int(input())
z = []
for i in range(n):
    num = int(input())
    if num == 0:
        z.pop()
    else:
        z.append(num)
print(sum(z))

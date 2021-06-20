# 백준 1110 하중 while 문 - 더하기 사이클

# 내 풀이(코드길이 460B)

a = input()
a = int(a)
# 위 두줄은 a = int(input()) 와 같다.

# while문을 돌린다. newN이 a와 같아질 때 까지. 한 번 돌때마다 cycle에 +1

def get_cycle(a):
   front = int(a/10)
   back = a%10
   sum = front + back
   newN = (back*10) + (sum%10)

   cycle = 1
   if a == newN:
      return cycle
   
   while a != newN:
      front = int(newN/10)
      back = newN%10
      sum = front + back
      newN = (back*10) + (sum%10)
      cycle += 1

   return cycle

print(get_cycle(a))


# 다른 사람의 풀이(코드길이 179B)

a = int(input())
check = a
count = 0

while True:
    sum = a//10 + a%10
    newN = (a%10)*10 + sum%10
    count += 1
    a = newN
    if newN == check:
        break

print(count)

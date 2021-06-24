# 백준 3052 1차원 배열 - 나머지

# Tip

arr = [1,1,1,2,2,3,3,3,4,5,5,5,5,6,6,6]
print(set(arr))

// {1, 2, 3, 4, 5, 6}


# 내 풀이

num_arr = []
for i in range(10):
   num_arr.append(int(input())%42)

print(len(set(num_arr)))

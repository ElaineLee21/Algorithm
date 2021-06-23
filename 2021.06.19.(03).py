# 백준 1021 중상 큐 - 회전하는 큐

# 내 풀이

n, m = map(int, input().split())
# 5 2

s = list(map(int ,input().split()))
# [2,3]

q = [i for i in range(1, n + 1)]
#  [1,2,3,4,5]

cnt = 0

for i in range(m):
   q_len = len(q) # 5
   q_index = q.index(s[i]) # 1
   if q_index < q_len - q_index: # 앞쪽이 더 가까우면
      while True:
         if q[0] == s[i]:
             del q[0]
             break
         else:
            q.append(q[0])
            del q[0]
            cnt += 1
   else: # 뒷쪽이 더 가까우면
      while True:
         if q[0] == s[i]:
            del q[0]
            break
         else:
            q.insert(0, q[-1])
            del q[-1]
            cnt += 1
            
print(cnt)

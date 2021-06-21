# 백준 1316 하 문자열 - 그룹 단어 체커

# 내 풀이

n = int(input())

group_word = 0

for word in range(n):
   word = input()
   non_group_word = 0
   for idx in range(len(word)-1):
# ^ 왜 -1이냐? 마지막 한단어는 비교 안해도 됨
      if word[idx] != word[idx+1]:
         new_word = word[idx+1:]
         if new_word.count(word[idx]) > 0:
            non_group_word += 1
   if non_group_word == 0:
      group_word += 1
print(group_word)

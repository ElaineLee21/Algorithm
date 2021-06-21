# 백준 1157 하 문자열 - 단어공부

# 내 풀이

word = input().upper()

# 그냥 list(word)하면 ['E', 'L', 'A', 'I', 'N', 'E']
# list(set(word))하면 ['N', 'I', 'A', 'L', 'E']
word_list = list(set(word))

# [1, 1, 1, 1, 2]
cnt = []

for char in word_list:
	 # count()는 괄호 안의 문자가 몇 번 등장하는지 뱉는 메소드
   count = word.count(char)
   cnt.append(count)

# max()는 괄호 안의 iterable(배열 등의 자료형)의 요소 중
# 가장 큰 값을 뱉음.
if cnt.count(max(cnt)) >= 2:
   print("?")
else:
   print(word_list[(cnt.index(max(cnt)))])
# max(cnt)는 2.
# cnt.index(2)는 4 (cnt 안에서 2가 4번 인덱스에 있다)
# word_list의 4번 인덱스는 'E'

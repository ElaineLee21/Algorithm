# 백준 2941 하 문자열 - 크로아티아 알파벳

# 내 풀이

one_char = ['c=','c-','dz=','d-','lj','nj','s=','z=']
string = input()

for char in one_char:
   string = string.replace(char, '_')

print(len(string))

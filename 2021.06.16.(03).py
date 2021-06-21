# 백준 1436 중 브루트포스 - 영화감독 숌

# 내 풀이

n = int(input())  # 몇번째 시리즈인지 n에 담김
cnt = 0
six_n = 666
while True:
    if '666' in str(six_n):  # '666'이 포함되었다면 cnt가 1 증가
        cnt += 1
    if cnt == n:  
        print(six_n)
        break
    six_n += 1

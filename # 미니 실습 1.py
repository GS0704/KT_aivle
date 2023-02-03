# 미니 실습 1
# Q) 리스트 원소의 최솟값 구하기 함수 min_of()를 작성하라.
# 아래 변수의 최솟값을 min_of() 를 활용하여 출력하라.

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

## 숫자만 되더라!
def min_of(n):
    Min = n[0]
    for i, j in enumerate(t) :
        print(i,j)
        if Min > j:
            Min = j
        
    return Min

print(min_of(t))


def min_of_v1(n):
    Min = n[0]
    for i in range(1, len(n)):
        if n[i] < Min:
            Min = n[i]
    return Min

print(min_of_v1(s))
print(min_of_v1(t))
print(min_of_v1(a))
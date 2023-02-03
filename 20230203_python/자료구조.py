# 원소를 역순으로 정렬하기

a = [2, 5, 1, 3, 9, 6, 7]

for i in range( len(a) // 2 ) :
    a[i], a[-i] = a[-i], a[i]
print(a)
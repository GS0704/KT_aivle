# 선형 검색 linear search

f_number = int(input("찾고자 하는 값을 선택하세요" ) )
a = [2, 5, 1, 3, 9, 6, 7]

def l_search(a):
    x = -1
    for i,j in enumerate(a):
        print(i,j)
        if j == f_number : 
            x = i
    return x

print(l_search(a))
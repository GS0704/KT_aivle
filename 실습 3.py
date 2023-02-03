# Q 리스트와 검색할 값을 사용자로부터 입력 받아서검색 값이 있는 인덱스를 출력하라.

a = list()
Count = int(input(" 몇개의 리스트를 만드시겠습니까? "))
for i in range(Count):
    b = int(input( " 숫자를 입력해 주세요"))
    a.append(b)
Search_number = int(input ("찾고자 하는 값을 입력해 주세요"))

# sort
def Sort(a):
    for i in range(len(a) + 1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a
a = Sort(a)
print(a)

def bin_search(b_list, Search_number):
    pl = 0
    pr = len(b_list)-1
    while(pl <= pr):
        pc =  (pl + pr)//2
        if b_list[pc] == Search_number:
            return pc

        if Search_number >= b_list[pc] :
            pl = pc + 1
        elif Search_number < b_list[pc] :
            pr = pc - 1
x = bin_search(a, Search_number)
print(f"{Search_number}는 a[{x}]에 있습니다")
# 선형 검색은 찾고자 하는 값이 뒤에 있을수록 길어짐
# 이진 검색은 정렬이 되어있다는 가정이 있어야함
b_list = [5, 7, 15, 28, 29, 31, 39, 58, 68, 70, 95]

Mid_size =  len(b_list)//2
Search_number = 39

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
x = bin_search(b_list, Search_number)
print(f"{Search_number}는 b_list[{x}]에 있습니다")
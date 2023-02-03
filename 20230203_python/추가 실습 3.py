# 컴퓨터 매장에는 n개의 부품이 있으며, 부품마다 정수 형태의 고유한 번호가 있다.
# 어느 날 손님이 m개 종류의 부품을 대량으로 구매하겠다며 부품의 재고유무를 문의하여ㅑㅆ다.
# 매장에 부품재고가 있는지 확인하는 프로그램을 작성하라.

# 매장이 가지고 있는 부품 리스트와 고객이 확인하고자 하는 부품 리스트를 입력받는다.
# 고객이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 nop를 출력한다.

# store = [2, 3, 7, 8, 9]
# customer = [7, 5, 9]
store = [1,2,3,7,8]
customer = [1,5, 8, 4, 6]
answer = list()


for j in customer:
    Flag = 0
    for i in store:
        if i == j :
            Flag = 1
            break
    if Flag == 1:
        answer.append("yes")
    if Flag == 0:
        answer.append("no")

print(answer)
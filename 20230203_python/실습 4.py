# Q) 리스트를 사용자로부터 입력 받아서 최소값과 최대값이 있는 인덱스를 출력하라.
Count = int(input("입력 받을 리스트 개수 : "))
x = list()
for i in range(Count):
    Input= int( input(f"{i + 1} 번째 입력 값 : ") )
    x.append(Input)

def Sort(a):
    for i in range(len(a) + 1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a

Sort_list = Sort(x)
print(f"Max = {Sort_list[0]}\nMin = {Sort_list[-1]}")
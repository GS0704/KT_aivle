
reverse_list = list()
Length = int(input("원소 수를 입력하세요 : "))
for i in range(Length):
    List_value = int(input (f"X{i}값을 입력하세요. : ") )
    reverse_list.append(List_value)
    
print("리스트를 역순으로 출력합니다.")

def list_reverse(a):
    for i in range( len(a) // 2 ) :
        print(i)
        a[i], a[ len(a) -1 - i ] = a[len(a) -1 - i ], a[i]
    return a

rl = list_reverse(reverse_list)
print(rl)
for i in rl:
    print(i) 
    

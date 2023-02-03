# Q) 2부터 1000사이의 수 중에서 소수를 리스트에 입력하고 출력하여라

# 소수는 자신과 1이외의 정수로 나누어 떨어지지 않는 정수이며, 2는 소수임

x = list()


for i in range(1,1001):
    Check = list()
    for j in range(2, i + 1):
        if i%j == 0:
            Check.append(i)
    if len(Check) == 1:
        x.append(i)
        
        

print(x)
print(len(x))
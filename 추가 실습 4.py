### 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다.
# 예를 들어 2와 7의 최소공배수는 14가 됩니다.
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

a = 10
b = 15
for i in range(max(a,b),a*b + 1):
    if i%a == 0 and i%b == 0 :
        print(i)


arr = [2,6,8,14]
def Max(arr):
    Max_value = 0
    Max_value2 = 0
    for i in range(len(arr)):
        if Max_value < arr[i]:
            Max_value2 = Max_value
            Max_value = arr[i]
    return Max_value
            
def Multi(arr):
    Mul = 1
    for i in arr:
        Mul*=i
    return Mul
print(Multi(arr))


def solution(arr):
    for i in range(Max(arr), Multi(arr)+1):
        Count = 0
        for j in range(len(arr)) :
            if i%arr[j] == 0:
                Count +=1
        if Count == 4:
            return i
            break
Solve = solution(arr)
print(Solve)
        
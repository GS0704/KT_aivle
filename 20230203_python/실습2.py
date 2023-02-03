# 리스트를 사용자로부터 입력 받아서 역순으로 정렬하여 리스트의 원소를 출력하여라.
# 원소 수를 미리 묻지 말고 코드가 실행될 수 있도록 하라.
# sort
def Sort(a):
    for i in range(len(a) + 1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a
a = [1,5,6,77,3,44,3]
a = Sort(a)
print(a)
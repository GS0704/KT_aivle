# 0부터 9까지 숫자 중 일부가 들어있는 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요


numbers = [1,2,3,4,6,7,8,0]


def solution(numbers):
    empty_numbers = list()

    for i in range(0,10):
        Check = 0
        for j in numbers:
            if i == j :
                Check = 1
                break
        if Check != 1 : 
            empty_numbers.append(i)
            
    Sum = 0
    for i in empty_numbers:
        Sum += i
    return Sum

print(solution(numbers))
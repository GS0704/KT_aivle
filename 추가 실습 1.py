lottos = [44, 1, 0, 0, 31, 25]
# lottos = [0,0,0,0,0,0]
win_nums = [31, 10, 45, 1, 6, 19]

def Sort(a):
    for i in range(len(a) + 1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return a
S_lottos = Sort(lottos)
print(S_lottos)
S_win_nums = Sort(win_nums)
print(win_nums)

Count = 0
Zero_Count = 0
Max_Rank = 7
Min_Rank = 7
for i,j in enumerate(S_lottos):
    if S_lottos[i] == 0:
        Zero_Count += 1             
    for k, l in enumerate(S_win_nums):
        if S_lottos[i] == S_win_nums[k]:
            Count +=1
# 가장 낮은 순위
Max_Rank -= Count
if Count == 0:
    Max_Rank = 6
# 가장 높은 순위
Min_Rank = Min_Rank - Zero_Count - Count

print(Min_Rank , Max_Rank)


# 맞춘 개수 만큼 증가

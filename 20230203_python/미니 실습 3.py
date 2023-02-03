b = [2,5,1,3,9,6,7]
S = 7
def seq_search_sentinel(b,key):
    a = b.copy()
    a.append(key)

    i = 0
    Count = 0
    while True:
        Count += 1
        if a[i] == key:
            break
        i += 1

    return (-1, Count) if i == len(b) else (i,Count)


def seq_search(a, key):
    i = 0
    Count =0
    while True:
        Count += 1
        if i == len(a):
            return (-1, Count)
        Count += 1
        if a[i]== key:
            return (i, Count)
        i += 1
    

x = seq_search_sentinel(b,S)
x1 = seq_search(b,S)
print(x)
print(x1)
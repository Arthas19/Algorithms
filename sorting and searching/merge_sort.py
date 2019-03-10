import math
from math import inf

def merge(list, l, m, r):
    p = m - l + 1
    q = r - m

    ll = list[l:l+p]
    ll.append(inf)

    rr = list[m+1:m+1+q]
    rr.append(inf)

    i, j = 0, 0

    for k in range(l, r+1):
        if ll[i] < rr[j]:
            list[k] = ll[i]
            i += 1
        else:
            list[k] = rr[j]
            j += 1

def mergeSort(list, l, r):
    if l < r:
        m = (l+r) // 2
        mergeSort(list, l, m)
        mergeSort(list, m+1, r)
        merge(list, l, m, r)

list = [3, 4, 5, 2, 6, 55, 3, 3, 24, 17, 14, 413, 3, 100, 232, 3445, 435, 122, 34, 155, 91, 12, 1]

mergeSort(list, 0, len(list)-1)

print(list)


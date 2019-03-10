from random import randint

def partition(list, p, r):
    x = list[r]
    i = p - 1

    for j in range(p, r):
        if list[j] <= x:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i+1], list[r] = list[r], list[i+1]

    return i+1

def randPartition(list, p, r):
    i = randint(p, r)
    list[i], list[r] = list[r], list[i]
    return partition(list, p, r)

def randQuickSort(list, p, r):
    if p < r:
        q = randPartition(list, p, r)
        randQuickSort(list, p, q-1)
        randQuickSort(list, q+1, r)
        

list = [3, 4, 5, 2, 6, 55, 3, 3, 24, 17, 14, 413, 3, 100, 232, 3445, 435, 122, 34, 155, 91, 12, 1]
randQuickSort(list, 0, len(list)-1)

print(list)
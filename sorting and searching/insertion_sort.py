def insertionSort(list):
    for i in range(len(list)):
        key = list[i]
        j = i-1
        while j>=0 and list[j] > key:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = key

list = [3, 4, 5, 2, 1, 6, 55, 3, 3, 24, 17, 14, 413, 3, 100, 232, 3445, 435, 122, 34, 155, 91, 12]

print(list)

insertionSort(list)

print(list)

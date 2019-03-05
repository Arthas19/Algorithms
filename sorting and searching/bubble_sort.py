
def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

list = [3, 4, 5, 2, 6, 55, 3, 3, 24, 17, 14, 413, 3, 100, 232, 3445, 435, 122, 34, 155, 91, 12, 1]

print(list)

bubble_sort(list)

print(list)

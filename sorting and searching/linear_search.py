def linearSearch(list, num):
    for i in range(len(list)):
        if list[i] == num:
            return i
    return False

list = [3, 4, 5, 2, 6, 55, 3, 3, 24, 17, 14, 413, 3, 100, 232, 3445, 435, 122, 34, 155, 91, 12, 1]

print(list)

print("Index", linearSearch(list, 100))

print("Index", linearSearch(list, 19))

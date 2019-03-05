
def recursiveBinarySearch(list, x, lower = 0, upper = 0):
    if upper == 0:
        upper = len(list)-1

    if lower > upper:
        return False

    mid = (lower + upper) // 2

    if list[mid] == x:
        return mid

    if list[mid] < x:
        return recursiveBinarySearch(list, x, mid+1, upper)
    else:
        return recursiveBinarySearch(list, x, lower, mid-1)

def iterativeBinarySearch(list, x):
    lower, upper = 0, len(list)-1

    while lower <= upper:
        mid = (lower + upper) // 2

        if list[mid] == x:
            return mid
        
        if list[mid] < x:
            lower = mid+1
        else:
            upper = mid-1

    return False

list = [1, 2, 3, 3, 3, 3, 4, 5, 6, 14, 17, 24, 34, 55, 91, 100, 122, 155, 232, 413, 435, 3445]

print(list)

print("Index", recursiveBinarySearch(list, 155))

print("Index", recursiveBinarySearch(list,  19))

print("Index", iterativeBinarySearch(list, 232))

print("Index", iterativeBinarySearch(list,   0))


def recursiveBinarySearch(list, el, lower = 0, upper = None):
    if upper == None:
        upper = len(list)-1

    if lower > upper:
        return False

    mid = (lower + upper) // 2

    if list[mid] == el:
        return mid

    if list[mid] < el:
        return recursiveBinarySearch(list, el, mid+1, upper)
    else:
        return recursiveBinarySearch(list, el, lower, mid-1)

def iterativeBinarySearch(list, el):
    lower, upper = 0, len(list)-1

    while lower <= upper:
        mid = (lower + upper) // 2

        if list[mid] == el:
            return mid
        
        if list[mid] < el:
            lower = mid+1
        else:
            upper = mid-1

    return False

# in order for binary search to work correctly, list must be already sorted
list = [1, 2, 3, 3, 3, 3, 4, 5, 6, 14, 17, 24, 34, 55, 91, 100, 122, 155, 232, 413, 435, 3445]

print(list)

print("Index", recursiveBinarySearch(list, 155))

print("Index", recursiveBinarySearch(list,  19))

print("Index", iterativeBinarySearch(list, 232))

print("Index", iterativeBinarySearch(list,   0))

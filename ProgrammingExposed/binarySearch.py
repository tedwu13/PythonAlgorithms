def binarySearch(array, lower, upper, target):
    midIndex = (lower+upper) / 2

    found = False

    if array[midIndex] == target:
        found = True
    elif array[midIndex] < target:
        return binarySearch(array, lower, midIndex-1, target)
    elif array[midIndex] > target:
        return binarySearch(array, midIndex+1, upper, target)
    else:
        return False



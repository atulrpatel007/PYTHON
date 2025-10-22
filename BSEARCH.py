def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(arr, 10))
print(binarySearch(arr, 3))
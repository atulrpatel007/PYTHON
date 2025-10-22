def InsertionSort(array):
    n = len(array)
    if n <= 1:
        return array
    for i in range(n):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j],array[j-1]= array[j-1],array[j]
            j=j-1
    return array

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,7,8,9,12,0,2,1]
print(InsertionSort(L))
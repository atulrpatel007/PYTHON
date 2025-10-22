def Insert(arr, a):
    n = len(arr)
    if n == 0:
        return [a]
    if a >= arr[-1]:
        return arr + [a]
    else:
        return Insert(arr[:-1], a) + arr[-1:]

def Isort(arr):
    n = len(arr)
    if n == 0:
        return arr
    L = Insert(Isort(arr[:-1]), arr[-1])
    return L


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,7,8,9,12,0,2,1]
print(Isort(A))
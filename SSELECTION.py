def searchselection(L):
    n = len(L)
    if n == 0:
        return L
    for i in range(n):
        mpos = i
        for j in range(i+1, n):
          if L[j] < L[mpos]:
              mpos = j
          (L[i], L[mpos]) = (L[mpos], L[i])
    return L
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,7,8,9,12,0,2,1]
print(searchselection(L))
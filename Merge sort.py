def Merge(A,B):
    m,n=len(A),len(B)
    C,i,j,k=[],0,0,0
    while k < m+n:
        if i == m :
            C.extend(B[j:])
            k = k + (n-j)
        elif j == n:
            C.extend(A[i:])
            k = k + (m-i)
        elif A[i] < B[j]:
            C.append(A[i])
            k = k + 1
            i = i + 1
        else:
            C.append(B[j])
            k = k + 1
            j = j + 1
    return C

def MergeSort(l):
    n = len(l)
    if n <= 1:
        return l
    L = MergeSort(l[:n//2])
    R = MergeSort(l[n//2:])
    B = Merge(L,R)
    return B
a=[0,43,432,1,1,2,42,32]
b=[1,2,3,4,5,6,7,8,9]
print(MergeSort(a))
print(MergeSort(b))
print(Merge(MergeSort(a),MergeSort(b)))
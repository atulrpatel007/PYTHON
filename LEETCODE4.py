class Solution(object):
    def findMedianSortedArrays(self, n1, n2):
        n=n1+n2
        n.sort()
        a=len(n)
        if len(n)%2==0:
            return (n[len(n)/2]+n[(len(n)-2)/2])/2.0
        else :
            return n[(len(n)-1)/2]
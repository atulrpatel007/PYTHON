import numpy as n
a=[42]
b=[1,2,3,4,5]
c=[[1,2,3],[4,5,6]]
d=[[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]
print(a,"\n")
print(b,"\n")
print(c,"\n")
print(d,"\n")
e=n.array(42)
f=n.array([1,2,3,4,5])
g=n.array([[1,2,3],[4,5,6]])
h=n.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(e,"\n",e.ndim,"\n")
print(f,"\n",f.ndim,"\n")
print(g,"\n",g.ndim,"\n")
print(h,"\n",h.ndim,"\n")
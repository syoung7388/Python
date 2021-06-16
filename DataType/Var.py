#list 복사
a= [1,2,3,4,5]
b=a
print(b)
print(id(a))
print(id(b))
print(a is b)
a[1]=8
print(b)


#[:] 같이 변경 X
a=[1,2,3]
b = a[:]
a[1] = 5
print(b)
print(a)

#copy 동일특성 [:]
from copy import copy
a = [1,2,3]
b = copy(a)
print(b is a)

#변수 만드는법

a,b = ('p','b')
(a, b) = 'p','b'

[a,b] = ['p','b']

a=b='b'

a,b = (3, 4)
a,b = b,a
print(a)
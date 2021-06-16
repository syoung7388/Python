#List 인덱싱
a=[1, 2, 3]
print(a[0]+a[2])
print(a[-1]) #마지막 요소
a=[1, 2, 3,[5, 6,7]]
print(a[3])
print(a[3][0])

#List 슬라이싱

b = [1,2,3,4,5]
print(b[0:2])
print(b[:2])
print(b[2:])

c= [1,2,3,[6,7,8],4,5] #중첩 슬라이싱
print(c[2:4])
print(c[3][:1])

print(b+c)
print(b*3)
print(len(b))

print(str(c[0])+"위")


#리스트 수정, 삭제

a[2] = 10
print(a)

del a[3]
print(a)

del a[1:]
print(a)


#리스트 관련 함수

#append

a.append(0)
print(a)
a.append("ss")
print(a)

#sort
a= [5,6,6,3,2,1]
b= ['a','s','f','e']
a.sort()
b.sort()
print(a)
print(b)

#reverse
a.reverse()
print(a)

#index (위치 반환)
print(a.index(6)) #존재 안하면 오류

#insert
a.insert(0, 4)
print(a)

#remove
a.remove(6)
print(a)

#pop
print(a.pop())
print(a)
print(a.pop(2))
print(a)

#count
print(a.count(3))

#extend

a= [1,2,3]
b= [4,5,6]
a.extend(b)
print(a)
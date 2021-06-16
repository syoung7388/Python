#True, Falses

print(1!=1)

a=[1,2,3,4]
while a: #a가 참일때 , 즉 []전까지
    print(a.pop())

if[]:
    print("참")
else:
    print("거짓")

print(bool('python'))#T
print(bool('')) #F
print(bool([1,2,3,4]))#T
print(bool([]))#F
print(bool(0))#F
print(bool(3))#T

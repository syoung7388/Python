s1 = set([0,1,2,3])
print(s1)

s2 = set("Hi, Json")
print(s2)

#set특성) 중복 하용 안함, 순서 없음

#list tuple로 변환가능
print(list(s1))
print(tuple(s1))


#교집합, 합집합, 차집합

s1 = set([1,2,3,4,5])
s2 = set([7,6,3,4,5])

print(s1 & s2) #교집합
print(s1.intersection(s2))

print(s1|s2) #합집합
print(s1.union(s2))

print(s1-s2) #차집합
print(s2-s1)
print(s1.difference(s2))


#관련함수

s1.add(9) #하나
print(s1)

s1.update([9,10,11]) #여러개
print(s1)

s1.remove(11)
print(s1)



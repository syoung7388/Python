#Map과 유사함


#추가 삭제

a={1:'a'}
a[2] = 'b'
print(a)
a['name'] = '김수영'
print(a)

del a['name']
print(a)

#Key값으로 값얻기
print(a[1])

#Key 중복 불가 / ListX
a= {'a':1, 'a':2}
print(a)


#getKey

a= {1:0, 2:1, 3:4, 4:5}
for k in a.keys():
    print(k)

print(list(a.keys()))

#getValues
print(a.values())

#getKeys &getValues
print(a.items())

#Key:Value 모두 지우기
a.clear()
print(a)


# Key로 value얻기
a={'name':'김수영', 'job': '취준', 'age': 25}
print(a.get('name'))
print(a.get('a','하잉')) #default

#안에 있는지 조사
print('name' in a)

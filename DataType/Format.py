##format

# 오른쪽 정렬
a = "{0:>10}".format("Hi")
print(a)

# 왼쪽 정렬
a = "{0:<10}".format("Hi")
print(a)


# 가운데 정렬
a = "{0:^10}".format("Hi")
print(a)

# 공백
a = "{0:=^10}".format("Hi")
print(a)


#소수점 format
y= 3.444444555
x = "{0:0.4f}".format(y)
print(x)

#왼쪽정렬
y= 3.444444555
x = "{0:<10.4f}".format(y)
print(x)

#오른쪽정렬
y= 3.444444555
x = "{0:>10.4f}".format(y)
print(x)

##f


#문자열 format

name = "김수영"
age =25
print(f'나의 이름은{name}입니다. 나의 나이는 {age}입니다.')

#문자열 format - 더하기
print(f'나의 이름은{name}입니다. 나의 내년 나이는 {age+1}입니다.')


#배열일 경우

d = {'name':'장보영', 'job':'간호사'}
print(f'나의 이름은 {d["name"]}, 직업은 {d["job"]}')


#정렬
print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')


#소수점
y= 5.88888
print(f'{y:0.4f}')
print(f'{y:10.4f}')

#퀴즈
print(f'{"python":!^12}')
#count
a="hobby"
print(a.count('b'))
#find
print(a.find('y'))
print(a.find('k')) # 존재 않하면 -1 return
#index
print(a.index('h')) #없으면 오류 발생

#join
print(",".join(a))
b= ['a','b','c','d']
print(",".join(b))

#대문자
print(a.upper())
#소문자
print(a.lower())

#공백 지우기
h = "  hi  "
print(h.lstrip())
print(h.rstrip())
print(h.strip())


#문자열 변경

goal ="I love Time"
print(goal.replace("Time", "유아인"))

#문자열 나누기
print(goal.split())
print(",".join(goal).split(","))
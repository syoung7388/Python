money= True
if money:
    print("돈이다")
else:
    print("FF")

#비교연산자
# x<y | x>y | x == y  | x != y | x<= y | x>=y
money = 500
if(money != 600):
    print("!600")
else:
    print("600")

#and | or | not

print (1 not in[1,2,3])


#pass 아무일 아니게 설정
if(money != 700):
    pass
else:
    print("zz")

#elif =else if

#한줄 조건부식

score= 80
message="su" if score>70 else "fale"
print(message)

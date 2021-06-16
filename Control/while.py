

treeHit = 0
while treeHit < 10:
    treeHit += 1
    print(treeHit)
    if treeHit == 10:
        print("pass")


#prompt
prompt = """
    1.A
    2.B
    3.C
    4.D
    Enter number: """

number = 0
while number != 4:
    print(prompt)
    number= int(input())

#break
coffee = 2
while True:
    money = int(input("돈을 넣어주세요 : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print("거스름돈: %d + 커피" %(money - 300))
        coffee -= 1
    else:
        print("돈을 다시 돌려줌")
    if(coffee == 0):
        break

#continue
a=0
while a<10 :
    a += 1
    if a % 2 == 0 :continue
    print(a)


list = ['one', 'two', 'three']
for i in list :
    print(i)

a= [(1,5),(2,8),(3,9)]
for(first, last) in a:
    print(first +last)

score = [10 , 50, 70, 80, 90]
number = 0
for s in score:
    number += 1
    if s < 20:
        print(f"{number} 번 학생 등급: Low")
    elif (s <  70):
        print(f"{number} 번 학생 등급: Mid")
    else:
        print(f"{number} 번 학생 등급: Hig")

#continue , range

add =0
for i in range(1,11):
    add += i
print(add)

marks = [90, 25, 67, 46]
for number in range(len(marks)):
    if marks[number] < 60:continue
    print(f"합격{number+1}번")


#구구단

for i in range(2,10):
    for j in range (1,10):
        print(f"{i}*{j}={i*j}", end=" ")
    print()

#리스트 내포
a= [1,2,3,4]
result = [num * 3 for num in a]
result2 = [num*3 for num in a if num%2==0]
print(result2)

result3 = [i*j for i in range(2,10) for j in range(1,10)]
print(result3)
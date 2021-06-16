#입력값이 여러개일때

def add_many(*args):
    result = 0

    for i in args:
         result += i
    return result
print(add_many(1,2,3,4,5))

def add(choice, *args):
    if(choice == "add"):
        result = 1
        for i in args:
            result += i

    elif (choice == "mul"):
        result = 1
        for i in args:
            result *= i
    return result

print(add('mul', 1,2,3,4,5))

#kwards

def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(a=3)

#함수의 결과값은 언제나 하나

def add_and_mul (a,b):
    return a+b , a*b
print(add_and_mul(4, 5))

#튜플로 받기
result1, result2 = add_and_mul(4, 5)
print(result1)


#매개변수 초기값 미리 설정
def say(name, old, man = False):
    print(f"나의 이름은{name}입니다.나이는 {old}살입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다")
say("김수영", 25)
say("김수영", 25, True)

#함수 안에서 선언한 변수의 범위? 안꺼눈 안, 밖은 밖=> 해결책: return, global
a=1
def vartest(a):
    a += 1
vartest(a)
print(a)


b= 1
def BB():
    global b
    b = b+1
BB()
print(b)


#람다

add = lambda a, b: a+b
result = add(3, 4)
print(result)





#r 읽기모드, w 쓰기, a 추가

# f = open("하잉.txt", 'w')
# f.close()

# f = open("C:/Users/l10-morning/Desktop/PythonBasic/vv.txt", 'w')
# for i in range(1,11):
#    data = f"{i}번째 줄입니다."
#    f.write(data)
#
# f.close()

#read
f = open("C:/Users/l10-morning/Desktop/PythonBasic/dd.txt", 'r')
data = f.read()
print(data)

while True:
    line = f.readline()
    if not line: break
    print(line)

lines = f.readlines()
print(lines)


f.close()

#더하기
f = open("C:/Users/l10-morning/Desktop/PythonBasic/a.txt", 'a')
for i in range(11, 20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()


#with 문과 함게하기
with open("foo.txt","w") as f:
    f.write("Loooo")


#import

import sys

args = sys.argv[1:]
for i in args:
    print(i)
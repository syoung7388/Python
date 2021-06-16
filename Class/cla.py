class Cal:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result
    def sub(self, num):
        self.result = self.result-num
        return self.result

cal1 = Cal()
cal2 = Cal()
print(cal1.add(5))
print(cal2.add(8))
print(cal2.sub(8))


class Fourclass:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = Fourclass()
a.setdata(4,2)
print(a.first)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

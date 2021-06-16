class Fourclass:
    def __init__(self, first, second): #생성자
        self.first = first
        self.second = second
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

class MoreFourcal(Fourclass):
    def pow(self):
        result = self.first ** self.second
        return result
a= MoreFourcal(3,4)
print(a.add())
print(a.pow())


#Overriding

class SafeFourCal(Fourclass):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second

a = SafeFourCal(4,3)
print(a.div())

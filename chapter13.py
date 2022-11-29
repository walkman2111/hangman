class Data:
    def __init__(self):
        self.nums = [1,2,3,4,5]
    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0,100)
print(data_two.nums)

class Shape():
    def __init__(self):
        pass
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,w,l):
        self.width = w
        self.length = l
    def calculate_primeter(self):
        primeter = self.width*self.length
        return primeter

class Square(Shape):
    def __init__(self,w):
        self.width = w
    def calculate_primeter(self):
        primeter = self.width**2
        return primeter
    def change_size(self,value):
        self.width += value


rcl = Rectangle(10,15)
scl = Square(10)

rcl.what_am_i()
scl.what_am_i()

scl.change_size(-5)
print(scl.width)
print(rcl.calculate_primeter())
print(scl.calculate_primeter())

class Horse():
    def __init__(self,c,s,r):
        self.color = c
        self.size = s
        self.rider = r

class Rider():
    def __init__(self,n):
        self.name = n

rdr = Rider("John")
hrs = Horse("Black",180,rdr)

print(hrs.rider.name)